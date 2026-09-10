# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b1dde1a-131b-3e0c-b9d2-18f8913fdfda | -13.285 | -61.8093 | 2026-09-10 16:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 97a92c0a-4969-3fc9-aa13-e2357e66f007 | -10.6798 | -46.0858 | 2026-09-10 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| a9b5fd4b-ef83-3bb5-a2da-f1b969c2d4b3 | -9.774 | -47.0693 | 2026-09-10 16:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 744.5 |
| 82800c6e-40af-3971-a164-474dd0019773 | -13.2094 | -61.7755 | 2026-09-10 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| d241593f-00e4-3b04-be64-0e7ee1c117e0 | -10.2358 | -45.3004 | 2026-09-10 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| d6c34b4d-7403-3e4a-a2a0-09a0e9d70188 | -3.387 | -59.4266 | 2026-09-10 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f1f036b2-5fd8-3537-99b6-deeff131d1a2 | -3.3504 | -59.4274 | 2026-09-10 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| fa28f4c7-3171-363a-8092-b25cefcb660a | -8.62 | -47.3451 | 2026-09-10 16:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 63ac6254-cb89-37f4-b318-4bd250b3df0e | -8.6012 | -47.347 | 2026-09-10 16:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 331.7 |
| c53c488c-a2a9-3d58-b201-30e32aad66ec | -8.9873 | -65.4379 | 2026-09-10 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c645e40a-7f1c-3590-95fa-fb4a0ba86836 | -13.2476 | -61.7536 | 2026-09-10 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8cb62102-da22-322f-aba7-489151d2da9c | -6.7077 | -45.4635 | 2026-09-10 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 067cb603-7fcc-3406-99ea-d2f6c1913dba | -3.3688 | -59.4079 | 2026-09-10 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 09d2b3b0-46e4-38b8-800a-d4e08b0081b6 | -10.2372 | -45.2087 | 2026-09-10 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 791ba153-a96a-36eb-8463-25d2ef33b875 | -10.2365 | -45.2546 | 2026-09-10 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 2b76a7ed-e051-3fc5-a512-99380aa127fa | -9.793 | -47.0672 | 2026-09-10 16:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 9d313622-9ec2-3ff5-895e-246b62180c7d | -8.631 | -66.5473 | 2026-09-10 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4a6fff9b-ebe3-3471-9bac-f97c482e2a17 | -3.3687 | -59.427 | 2026-09-10 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 3d2cfd0d-9496-3838-850b-36ff4485a4e5 | -13.6325 | -59.475 | 2026-09-10 16:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2ebb0054-db84-31d3-884f-a18af52acec0 | -10.7084 | -50.6212 | 2026-09-10 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4e2876d8-ef66-3440-9c82-b2748e2787f2 | -13.285 | -61.8093 | 2026-09-10 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 73c2b676-7e18-3c53-b3b1-a7780ebce47e | -8.6009 | -47.369 | 2026-09-10 16:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| bd5f6541-a326-3e65-ae31-f6b482c006a9 | -8.6311 | -66.5287 | 2026-09-10 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 186.1 |
| 000eb80a-5d98-3ab1-9da4-2bd0f6b365a7 | -13.304 | -61.8081 | 2026-09-10 16:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4d124b27-d54c-3f98-b910-20140a72503f | -13.3298 | -61.1064 | 2026-09-10 16:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 39ea20f6-314f-3f20-9114-9ee61ca4b322 | -10.2362 | -45.2775 | 2026-09-10 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 13aeb22f-2388-3d9f-870a-47d6b8965f9b | -10.7582 | -45.9397 | 2026-09-10 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 1e3b36b7-0215-3786-ad24-317bcaa67d64 | -8.9428 | -63.2797 | 2026-09-10 16:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| cf08205c-b034-3a29-81ef-8ca9a3f7e3ae | -10.6812 | -45.995 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 8cddc1d1-83e8-394b-ab0f-9e55ee0f3e5e | -10.6801 | -46.0631 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |
| a1fe74f2-1d8d-3155-aeb4-6e0720fa8466 | -9.7131 | -65.0013 | 2026-09-10 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| e317b0e6-8360-37d4-8c08-815f4d4ffdfd | -13.2852 | -61.7899 | 2026-09-10 16:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f2236e02-bb67-3bed-ab09-89a370462d8c | -10.6985 | -46.106 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 4b35893a-23ab-30c3-9c01-5216172451b1 | -8.6012 | -47.347 | 2026-09-10 16:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 8bbd2cec-6f46-3027-92db-5a6f908b8b36 | -10.2365 | -45.2546 | 2026-09-10 16:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 96f532d4-4feb-3e46-ad76-77d1c6b1cd84 | -8.9875 | -65.4006 | 2026-09-10 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b51f61f1-26ec-3b1c-981c-149eef15f492 | -1.4944 | -54.2563 | 2026-09-10 16:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| eae4cbdc-bed4-3c13-b90a-9748427b0e96 | -13.3298 | -61.1064 | 2026-09-10 16:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 04dda9ea-fac5-3340-9c42-b1d6ecbb0635 | -10.6981 | -46.1287 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 455.7 |
| 1320755b-89ff-3462-81b2-e2d09ea1689d | -10.2362 | -45.2775 | 2026-09-10 16:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 009dc02c-b6b3-36f0-a7d7-58ec1aa503e8 | -10.7084 | -50.6212 | 2026-09-10 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d15c5b9f-93d6-3e44-9f2b-f0bf01bcb807 | -10.7274 | -50.6192 | 2026-09-10 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 5db5be7c-1dad-36b9-b7d4-165fcf7c7ae4 | -10.6798 | -46.0858 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 343.0 |
| 9a9fc729-bfa8-34c7-b485-e057346a3d3e | -10.6794 | -46.1085 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 676.0 |
| 9bc91e8f-14f1-379e-8a94-30d07a14bcd7 | -10.6808 | -46.0177 | 2026-09-10 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 3031dbbd-b8fc-3bf3-9c14-e1d692d1735c | -10.6985 | -46.106 | 2026-09-10 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 12b0a437-7124-30df-8970-a07ba4955e84 | -13.2476 | -61.7536 | 2026-09-10 16:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8c2233e4-1c2b-3b63-b559-849621aa5a3b | -8.532 | -63.898 | 2026-09-10 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 2c906337-9788-3dfb-b79f-73f2961bbff2 | -13.2297 | -61.6384 | 2026-09-10 16:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 331224dc-e165-3add-9c42-a53db4da27d5 | -8.9876 | -65.3819 | 2026-09-10 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| fd2c001a-7196-3e83-9109-9bc875c94ee3 | -10.7395 | -45.9194 | 2026-09-10 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 834c5af3-f2fc-3045-a4e7-897963835b47 | -13.2094 | -61.7755 | 2026-09-10 16:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 37606a4e-5715-36cc-8346-9a0c3521e1d0 | -10.6798 | -46.0858 | 2026-09-10 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 440.9 |
| 1bf28390-f831-3715-8ebd-0f73cdea51e1 | -3.8462 | -58.8985 | 2026-09-10 16:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 155.1 |
| d74cb5f7-89df-3473-aae4-c1ca3bd79440 | -8.9873 | -65.4379 | 2026-09-10 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f53bd5c2-99d1-3391-831a-2f52e8ac0d6a | -10.2358 | -45.3004 | 2026-09-10 16:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cb20d164-03d8-3f87-9b4d-57ab091ec2fc | -13.2092 | -61.795 | 2026-09-10 16:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 51b42886-9718-3428-8f80-a35d64b01e04 | -10.7582 | -45.9397 | 2026-09-10 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| fdf0af10-1e2f-37d7-a78d-ebaf4d3103bc | -10.6981 | -46.1287 | 2026-09-10 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 294.7 |
| a7aff846-2ed1-3505-aa95-a667b3df931c | -13.2667 | -61.7329 | 2026-09-10 16:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| f898fced-141e-3025-89fb-2c24ea815c5a | -10.2362 | -45.2775 | 2026-09-10 16:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| eea0c517-747a-302c-83d2-d34986f0d9e5 | -13.2284 | -61.7743 | 2026-09-10 16:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 908361c9-a64f-336d-9df7-09817e9f2b75 | -1.4944 | -54.2563 | 2026-09-10 16:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2bac9beb-d798-3840-8d45-bb081fe6fa7b | -8.6012 | -47.347 | 2026-09-10 16:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 420fe174-bf2f-3219-8f75-81e36d836129 | -13.2094 | -61.7755 | 2026-09-10 16:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f8e4dd6e-9825-3906-b878-ec9c9330b25e | -10.7582 | -45.9397 | 2026-09-10 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 4513ae9c-f4fb-36db-990e-9bae8b737be8 | -10.6985 | -46.106 | 2026-09-10 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 30744c51-ba52-3a5f-adac-3af8075f71b9 | -10.2556 | -45.2521 | 2026-09-10 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 166.9 |
| ecfd1d21-0703-333a-96f8-c3e5f3679f1d | -9.774 | -47.0693 | 2026-09-10 16:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 366.5 |
| 31ff00e4-543d-3594-a87c-e150a9bac246 | -13.6704 | -59.4916 | 2026-09-10 16:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| afb937d5-3294-3949-90d0-9066b06a93cf | -13.209 | -61.8144 | 2026-09-10 16:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 87b89e80-4a65-345a-93d6-2be6330d5467 | -10.6981 | -46.1287 | 2026-09-10 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 5a59a6d4-0490-3b87-a249-5df9ef4350da | -10.7487 | -60.7676 | 2026-09-10 16:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 203550b4-e6a9-3048-aca6-fc288f155cc1 | -10.6798 | -46.0858 | 2026-09-10 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 2af6f27d-f161-32f4-a629-4949c41ddb3f | -10.2358 | -45.3004 | 2026-09-10 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 7a901dd7-4663-32a6-8e64-e6b08df605af | -10.6794 | -46.1085 | 2026-09-10 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 654.2 |
| e9ea93c2-27c6-3429-b0ce-488906f3747a | 2.1818 | -50.8985 | 2026-09-10 16:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 45e9e15b-9f7d-31db-9440-f66196cb3da3 | -10.8047 | -60.7837 | 2026-09-10 16:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 28eacf69-5550-3162-a23d-93a192eaa5d2 | -10.2559 | -45.2292 | 2026-09-10 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| dbfdfa7f-d418-366d-abc1-ba8e5337b23e | -10.0815 | -45.4567 | 2026-09-10 16:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 36fa78b5-bb64-385a-add0-8bf2a2dc0a69 | -8.631 | -66.5473 | 2026-09-10 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2d3a81ff-9240-3ca3-94fc-a16bf20a4a06 | -13.2092 | -61.795 | 2026-09-10 16:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |


