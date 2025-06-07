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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84dc5f2e-6aa6-3c50-99f9-e5045b5e29f8 | -12.70244 | -58.02308 | 2025-06-07 06:03:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b73b5145-ede7-3bd0-b5ea-5153273bf69c | -13.29119 | -57.93736 | 2025-06-07 06:03:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 190e0dd3-abb1-388b-bea1-2adae349b538 | -11.25935 | -60.7984 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc14a37-654c-3dd6-b439-5cd35c60f2c0 | -11.2593 | -60.80492 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bca3340-3f2e-3dce-ad1a-b9bd2e3fca30 | -11.25556 | -60.78772 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38a46fd9-afff-3466-822f-41463c8f8819 | -11.25887 | -60.8025 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1285797-a57e-3241-be67-43fd4d733c4e | -10.30335 | -57.13753 | 2025-06-07 06:03:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a87c08bf-3e72-3bcc-a9b7-5a6c6abfbbb2 | -11.26565 | -60.79499 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99f70c2b-412f-3691-bde3-dcade7f7aea9 | -11.83848 | -60.92266 | 2025-06-07 06:03:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab5cdc16-6f29-3c11-9939-5edee17b1ce1 | -11.25879 | -60.80897 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51ba560f-5774-3bee-a828-024bcab56540 | -11.54097 | -60.99584 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c491e03f-4669-3ee9-b36d-5202cd64b601 | -11.83799 | -60.92673 | 2025-06-07 06:03:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06a9ec6e-7e1d-34e4-90cc-e4cad52f52fd | -11.25838 | -60.80656 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd57dc55-aec7-36ad-a1cd-7d1726ecd5b9 | -12.10573 | -64.05772 | 2025-06-07 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b850612-fe05-33e4-b42c-bb2ede6546d0 | -11.26032 | -60.7968 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa86af0e-dd9c-364d-a789-7fff539def4d | -13.28411 | -57.9366 | 2025-06-07 06:03:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77d85802-331a-3a4c-b196-6de21f288dd8 | -11.90255 | -63.3278 | 2025-06-07 06:03:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9197898-ba1b-3a09-850a-592a37214f55 | -12.66653 | -58.2249 | 2025-06-07 06:03:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b33717c-1448-3ecb-af73-2b7b22ec319c | -9.41977 | -63.33553 | 2025-06-07 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4cdcd1b-7aaf-33d7-bb08-68e358cbf367 | -10.29616 | -57.1368 | 2025-06-07 06:03:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a3febfe-aa75-3d6c-b70b-b5482f58b5ff | -11.26517 | -60.79904 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e843f6d-7939-3657-b571-1da48f4a796b | -11.25983 | -60.79433 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26a5dd26-0b7b-3933-a300-b21daa8d913d | -11.25454 | -60.79589 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e08351f3-61d4-3c8c-862a-f3e8ee81f972 | -11.2647 | -60.80301 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf1b77c-aa26-3484-9eb9-b8ead8040f83 | -9.8188 | -67.41595 | 2025-06-07 06:03:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 970678d7-1e43-3923-8619-0f8081510c59 | -11.26084 | -60.79271 | 2025-06-07 06:03:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a98d3bf2-70e0-3afe-bb9c-953b0d932690 | -12.66722 | -58.21848 | 2025-06-07 06:03:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d55a376-9fe8-3ba8-a1b1-69138736f13c | -12.10101 | -64.05704 | 2025-06-07 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 369a143b-dcca-3220-a088-129dd3654e68 | -13.29826 | -57.93822 | 2025-06-07 06:03:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460f2731-1b8e-37b9-b88e-b924bd5853de | -6.9602 | -42.9052 | 2025-06-07 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 190edb9c-bf03-3ff3-a2d8-d05f9142512a | -7.7364 | -44.1592 | 2025-06-07 06:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 44fece11-f00c-384a-ba15-03d135ceb954 | -7.7176 | -44.1611 | 2025-06-07 06:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0976d96a-64cd-3657-a84f-efd71ac97532 | -5.6379 | -43.7175 | 2025-06-07 06:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 17ba1c53-9cc5-3969-8a67-b92182e30f72 | -7.7361 | -44.1823 | 2025-06-07 06:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8c27d859-d992-33b4-85c9-014bb7252c37 | -7.7364 | -44.1592 | 2025-06-07 06:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e75613c7-c03c-33b8-b185-bf7a778b22c6 | -6.9602 | -42.9052 | 2025-06-07 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| bc7b8b86-2d06-3b20-b943-5484b47cca77 | -7.7176 | -44.1611 | 2025-06-07 06:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8bd8171a-3cf2-3497-9848-103be8cafac8 | -7.7361 | -44.1823 | 2025-06-07 06:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f8be0e29-2691-3108-8267-e6a8cb5c036b | -7.7176 | -44.1611 | 2025-06-07 06:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 857813dc-6e8c-3629-8e04-536f5804ab37 | -7.7361 | -44.1823 | 2025-06-07 06:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bb6dc3a9-a542-3fe2-a328-8d62138dd993 | -7.7364 | -44.1592 | 2025-06-07 06:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8f4a8d8d-8323-3df6-9c3d-62588d830365 | -6.9602 | -42.9052 | 2025-06-07 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 92cf0a39-7762-3fb0-a128-4c764b6555d5 | -7.7361 | -44.1823 | 2025-06-07 06:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| fab2914b-e281-3e9c-a638-9dd729c045f5 | -5.6379 | -43.7175 | 2025-06-07 06:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c65eb7a5-6f56-399a-8310-07eb9938b276 | -7.7364 | -44.1592 | 2025-06-07 06:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e0d977d5-28a6-3052-b255-0a1db94946d3 | -6.9602 | -42.9052 | 2025-06-07 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| eb157878-f643-3afb-8972-5cfb6d08fafd | -7.7176 | -44.1611 | 2025-06-07 06:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 3749842f-2b24-32ea-b869-0c0aa2a78727 | -6.9602 | -42.9052 | 2025-06-07 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| d57ea2c7-9d1f-3683-86d0-8528b0603cab | -7.7176 | -44.1611 | 2025-06-07 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 575f5382-51ba-38ea-9693-bcbadfe6bda3 | -7.7364 | -44.1592 | 2025-06-07 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5c371c7d-9ac7-32e5-a036-8292dc25ac41 | -7.7361 | -44.1823 | 2025-06-07 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e54dc56d-aaaf-34c3-a619-bb67c2bf2fee | -6.9602 | -42.9052 | 2025-06-07 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 29bd3a16-0235-3c4d-ab4e-602d8f3d6679 | -7.7364 | -44.1592 | 2025-06-07 07:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7f3c5075-8af6-39a2-93f4-0e51716ba9e9 | -7.7361 | -44.1823 | 2025-06-07 07:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8e3c053c-20e8-301b-8888-0c7f6394de4e | -7.7176 | -44.1611 | 2025-06-07 07:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 619485c0-67ed-3fa3-9559-6cd96242504d | -6.9602 | -42.9052 | 2025-06-07 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| dc5341b1-d2a0-31da-bab3-c620532e2d62 | -7.7364 | -44.1592 | 2025-06-07 07:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e3eaed1b-5315-3461-92f7-b4f1f723816c | -7.7361 | -44.1823 | 2025-06-07 07:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 925ab08f-c501-3c39-a675-5a461cea1557 | -7.7176 | -44.1611 | 2025-06-07 07:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d4071182-9bac-395a-a877-c634c62e62d1 | -7.7361 | -44.1823 | 2025-06-07 07:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a89f42cb-cb14-3bf0-ab82-6382e03bacc6 | -7.7176 | -44.1611 | 2025-06-07 07:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2f50b8e7-8226-30f6-a4da-201ffaba46ea | -7.7364 | -44.1592 | 2025-06-07 07:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 56ddd394-2ba8-3926-8596-da8d4c80b3ef | -6.9602 | -42.9052 | 2025-06-07 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| aea59a8d-0b87-3461-a832-44c36441128b | -7.7364 | -44.1592 | 2025-06-07 07:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9ae4b086-bcaa-3694-8c19-e86759aa6063 | -6.9602 | -42.9052 | 2025-06-07 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| d07fdc8f-9e08-3ddf-a2b8-1bc4240a533b | -7.7361 | -44.1823 | 2025-06-07 07:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0392623f-844c-38e2-848c-d661d9dfa134 | -7.7361 | -44.1823 | 2025-06-07 07:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 98f83575-73bf-3538-970f-e3be5dab6889 | -7.7176 | -44.1611 | 2025-06-07 07:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 0db51246-8490-313a-90a7-03efac878462 | -7.7364 | -44.1592 | 2025-06-07 07:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 385d7221-1b19-3a09-82dd-dfddab9cd53d | -7.7361 | -44.1823 | 2025-06-07 07:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 480a3023-e7f0-3d81-9b3f-2bd407af458f | -7.7176 | -44.1611 | 2025-06-07 07:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| fa778983-77d4-3957-8ca5-9122649233f2 | -6.9602 | -42.9052 | 2025-06-07 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 2da687df-1abf-3f8e-82cc-0d3706fde949 | -7.7364 | -44.1592 | 2025-06-07 07:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| dc22aab5-da34-3fe5-ba26-ca9919ff8f8f | -7.7364 | -44.1592 | 2025-06-07 08:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 179222d5-bdde-3019-bc45-5c4d80044676 | -7.7361 | -44.1823 | 2025-06-07 08:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d0428cbb-380e-3eff-8108-e232e547cb39 | -7.7176 | -44.1611 | 2025-06-07 08:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b9eae754-9ea3-38e6-b24f-a673aaaa1dfa | -7.7361 | -44.1823 | 2025-06-07 08:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1ea56a4d-c575-367c-adb3-c08684f6f0de | -7.7364 | -44.1592 | 2025-06-07 08:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6aa30c91-a7cc-3ea3-a404-0687b6b0dbc3 | -7.7176 | -44.1611 | 2025-06-07 08:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 53cd1f8d-05d0-3a1e-a0be-8149ac4dbcb6 | -7.7364 | -44.1592 | 2025-06-07 08:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| af3678ac-0d8f-3ade-aaaa-a0c6712adefa | -7.7361 | -44.1823 | 2025-06-07 08:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1afcfe58-c9ff-37bf-9e89-bc00cf2c3b93 | -5.6379 | -43.7175 | 2025-06-07 10:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 744a4ac0-5e38-375d-80b7-305b82851f88 | -6.10055 | -43.9647 | 2025-06-07 12:42:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 18bcbd7a-96f6-3fb2-afaf-2d1e84d2f668 | -5.42107 | -43.19151 | 2025-06-07 12:42:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 5c07ee43-6264-36aa-b30e-f9ff79dd5135 | -5.42441 | -43.1658 | 2025-06-07 12:42:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| be24381d-7b2c-3ea7-a804-fa576af70d31 | -5.77603 | -43.48796 | 2025-06-07 12:42:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| db855550-da2e-34f2-8c5f-ac4ad6d75af4 | -6.0931 | -43.95816 | 2025-06-07 12:42:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 42052e66-20f6-3499-960c-f44cff36bcaa | -5.64202 | -43.70555 | 2025-06-07 12:42:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| be4bb1fc-9868-3e59-bbe2-d81c41e380e8 | -4.28104 | -43.31873 | 2025-06-07 12:42:00 | TERRA_M-T | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b93012e5-693e-3080-8f81-553a620c8f10 | -5.77967 | -43.61573 | 2025-06-07 12:42:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0a05b8f3-8957-323e-820d-4848043246c5 | -3.05095 | -49.4314 | 2025-06-07 12:42:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 101397f9-626d-3084-83fb-b69bc092f93d | -5.63897 | -43.72871 | 2025-06-07 12:42:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 0d2b3538-1715-3e91-82f4-448381c05bf7 | -3.04965 | -49.44042 | 2025-06-07 12:42:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3a94b5f4-da0b-3e00-b59c-e21a914dedc2 | -6.21054 | -43.31963 | 2025-06-07 12:42:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c64c27c3-b95a-3deb-bb03-06d63d96a6d0 | -6.24254 | -48.54925 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b25b0512-a49b-3925-883f-14deab44c925 | -9.40358 | -48.4394 | 2025-06-07 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c63f2d1a-1454-39d5-9b97-a3b134a3a3fd | -13.47069 | -56.85921 | 2025-06-07 12:44:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8f237b51-3c2f-31bf-998f-d4acb61390c1 | -6.90939 | -47.77848 | 2025-06-07 12:44:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| cf4419f8-debe-3e8f-a316-5190af1f4360 | -12.95854 | -46.75924 | 2025-06-07 12:44:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 497c184d-7c78-387f-a04e-db511b6ca556 | -9.16559 | -49.51624 | 2025-06-07 12:44:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README27.md)
