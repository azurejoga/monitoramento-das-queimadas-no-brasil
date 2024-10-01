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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07d102c7-85e9-34d4-b21f-e573c7d0f6af | -22.37 | -49.3477 | 2024-10-01 02:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| 984bf503-8d3c-3e61-a60b-dba32513331d | -22.3707 | -49.3244 | 2024-10-01 02:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 339.5 |
| 251d76a1-2351-3ab2-9c99-ea2b2b4b1274 | -22.3713 | -49.3011 | 2024-10-01 02:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 140.8 |
| 3484e866-fc9d-3c77-ba15-a0254588766b | -22.3916 | -49.3194 | 2024-10-01 02:17:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.2 |
| 486eb4f8-71ca-3773-b0b4-f2eb07a3f87b | -22.3922 | -49.2961 | 2024-10-01 02:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| eaffafd6-9213-3766-8ec3-d8b77b6b7dd6 | -23.0793 | -45.3951 | 2024-10-01 02:17:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 8da4fe88-99c0-323a-bfa3-b6828725f96a | -19.13176 | -57.49511 | 2024-10-01 02:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| b03de0ed-e122-3c68-85dc-84dcabb45de0 | -19.1289 | -57.50239 | 2024-10-01 02:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.8 |
| 46a95690-89ea-3fb2-80e2-dc968e38f077 | -19.12001 | -57.45836 | 2024-10-01 02:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.3 |
| 821400a9-d8e2-3bf3-a1ba-243609af0a3e | -5.9786 | -45.3847 | 2024-10-01 02:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e93b3127-7531-3c8a-b7c0-492f57644c44 | -5.9788 | -45.3621 | 2024-10-01 02:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7adf3d21-a137-347e-afc9-4e401dc0bb51 | -9.51688 | -68.57861 | 2024-10-01 02:26:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c5c51641-9bda-3abd-92e5-9868065d0a2e | -9.49665 | -68.50267 | 2024-10-01 02:26:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4bca5a02-4537-3d0f-968f-315bb5649de6 | -9.35116 | -68.8394 | 2024-10-01 02:26:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 180ba62f-efd2-31a7-aa53-fe45308dec9e | -9.30115 | -68.75014 | 2024-10-01 02:26:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c55198ed-555e-3bd9-89c5-dd3d0622d6aa | -9.27512 | -67.60651 | 2024-10-01 02:26:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 49f4cd8c-0c04-3b27-a0dc-187e1c09c4d7 | -9.26546 | -67.60797 | 2024-10-01 02:26:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d136781-188b-38a4-8ba1-363e90960602 | -9.04969 | -67.79497 | 2024-10-01 02:26:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 666cda54-bbfc-3afc-b81f-ef6641f75f09 | -9.03586 | -68.50329 | 2024-10-01 02:26:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2fad223b-dba1-3be1-b7e3-2558fce28517 | -11.66243 | -65.00966 | 2024-10-01 02:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 7df38e3a-97b3-3a62-bc33-198d9416215a | -11.66206 | -65.00327 | 2024-10-01 02:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b6ade513-acd9-3110-8ab9-eb1d9d6f7f12 | -11.66015 | -64.99482 | 2024-10-01 02:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 24ec8f76-a527-3839-a965-4fda933cf8de | -11.64899 | -64.99673 | 2024-10-01 02:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2b0d31c8-f612-35aa-9e8a-1411e89f007c | -10.89019 | -69.0932 | 2024-10-01 02:26:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2c2bfc0e-31cd-381d-91b7-572fbb1726cc | -10.71544 | -69.4249 | 2024-10-01 02:26:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3a4fefea-b331-30ee-8be8-a5319ef02597 | -10.71416 | -69.41587 | 2024-10-01 02:26:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d378636b-5acd-39a0-9088-ee8177234f99 | -10.70655 | -69.42621 | 2024-10-01 02:26:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ac5cca55-534f-3216-b2a6-2e7d2898d504 | -10.70528 | -69.41718 | 2024-10-01 02:26:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ac0caad6-5b8a-31d8-ab6f-91705a660543 | -10.68239 | -69.38364 | 2024-10-01 02:26:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff26c408-427e-3f32-9d0d-9ce276945297 | -10.54155 | -69.3057 | 2024-10-01 02:26:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 15eb459e-93d5-3f4b-9d19-b77ba792786a | -10.43035 | -69.23566 | 2024-10-01 02:26:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c246d07-bc32-3783-8c34-12b5d16e623a | -10.42231 | -68.59555 | 2024-10-01 02:26:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b824aef3-409a-34eb-944f-17e973e0966d | -10.42095 | -68.58605 | 2024-10-01 02:26:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fb4224e5-7ec6-3a8b-8afd-e8f9c57c75aa | -10.27151 | -68.76543 | 2024-10-01 02:26:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2b10fb2e-4345-390c-ad3d-ea28e71a56c9 | -10.12818 | -67.90131 | 2024-10-01 02:26:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2646c0a0-5d7c-3dfa-ac50-066e5c874393 | -10.12669 | -67.89113 | 2024-10-01 02:26:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fb4073cf-9df1-320a-9d18-4eacb15f4d90 | -10.08009 | -69.16592 | 2024-10-01 02:26:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e25474e-8a80-3b24-9bc1-f16216542df2 | -10.05257 | -68.58842 | 2024-10-01 02:26:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f65f77ad-42eb-3656-b6b4-20247064608c | -11.2591 | -43.3909 | 2024-10-01 02:26:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 774eee29-0bde-3329-8c65-aec2b76428d9 | -11.258 | -45.6682 | 2024-10-01 02:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 7b96e38e-4364-3cb9-add2-2dfb3b21f2a4 | -11.2584 | -45.6453 | 2024-10-01 02:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| e8f87086-f7ba-3114-aa2c-db33e541df0c | -11.2771 | -45.6656 | 2024-10-01 02:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 356e2463-6b92-3c00-a4bc-1cff5f911405 | -11.2775 | -45.6427 | 2024-10-01 02:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ad0db4cb-c544-391b-9cde-5d741919b6a3 | -11.6367 | -64.9999 | 2024-10-01 02:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dde35caf-33b6-345b-80d9-7de78dad01c0 | -11.6554 | -65.018 | 2024-10-01 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dcc856c3-ae95-3e23-a8cf-a86f6714eb99 | -11.6555 | -64.9991 | 2024-10-01 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 2a70153a-49b9-33bb-9ccc-75f18f696ca7 | -11.6556 | -64.9802 | 2024-10-01 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 132.1 |
| cc428def-72da-368b-bdac-969c56d4ed22 | -11.6743 | -64.9983 | 2024-10-01 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 06d16216-db48-33e8-b529-3e30285924f2 | -11.6744 | -64.9793 | 2024-10-01 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 76dd7006-0f2b-3535-a96d-92eadd9a0a10 | -12.1402 | -50.074 | 2024-10-01 02:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fdb8bd1a-53ea-3ca8-aca6-431485dad09c | -12.1406 | -50.0524 | 2024-10-01 02:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 1ed20a6c-67cc-3f70-866c-24550f4b4764 | -12.1593 | -50.0717 | 2024-10-01 02:26:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 918b98b8-a002-3654-b215-f6c882942167 | -12.6039 | -53.4879 | 2024-10-01 02:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| c0155443-6fe4-322e-9356-8e16809dca7e | -12.9245 | -51.2002 | 2024-10-01 02:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7f9f0173-298e-38c9-94a2-18f606aa2039 | -13.2112 | -51.2287 | 2024-10-01 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a811f821-19ff-328b-b2f1-1646f770e7af | -13.2116 | -51.2073 | 2024-10-01 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e292fe07-0868-3421-814b-c6e932c07cf6 | -13.2304 | -51.2262 | 2024-10-01 02:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0a2e801d-d343-3ed1-8a1f-2fef82e3c9b7 | -13.5765 | -51.1821 | 2024-10-01 02:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0b1a364d-622c-3852-b3a1-f44693b05851 | -13.595 | -51.2225 | 2024-10-01 02:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2b35eb61-c2a0-3e84-934f-66fb1bfe4d70 | -13.5954 | -51.2011 | 2024-10-01 02:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 411001fe-2516-3920-b0ef-08697b7e05b0 | -13.5957 | -51.1796 | 2024-10-01 02:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 259.2 |
| b3bbf9b8-21a5-3535-ab09-d84a12f9a892 | -13.5961 | -51.1582 | 2024-10-01 02:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2bd3d3cc-3a83-389f-b7c8-8460c27a57a9 | -14.7406 | -48.7498 | 2024-10-01 02:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 367c8ed7-5b86-318a-94c0-8760654eb02d | -15.0673 | -49.9115 | 2024-10-01 02:26:30 | GOES-16 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 09b8b4c6-b965-3126-8d55-6d3083af54b1 | -15.0678 | -49.8895 | 2024-10-01 02:26:30 | GOES-16 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| d7683e6a-28c2-3b55-abc2-bc8181e55eac | -15.9127 | -57.1733 | 2024-10-01 02:26:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 5b948168-8e9f-3ead-8ba8-db1c1e0aff10 | -16.1856 | -58.4417 | 2024-10-01 02:26:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 2970e279-4940-31fc-9c99-15779604ccaa | -16.1859 | -58.4215 | 2024-10-01 02:26:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 52d0e526-6ee1-3820-b292-10a4ee7b173f | -16.474 | -57.3553 | 2024-10-01 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 2efeb8e6-cbc9-3f86-ab5e-df37e18138ce | -16.4743 | -57.3349 | 2024-10-01 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 006a88bc-dd73-3e6f-9949-bb2810caca78 | -16.4935 | -57.3531 | 2024-10-01 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| b66b4669-495c-36bf-aeac-5c60ebd18d3e | -16.4939 | -57.3327 | 2024-10-01 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 29a8e34c-fb38-3f6b-af82-bffeaf359bed | -16.5131 | -57.3509 | 2024-10-01 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 7dd8918e-d179-3793-b183-ba299d71b46a | -16.5134 | -57.3305 | 2024-10-01 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| e44ad7f3-ba17-3e7e-b653-6c5de100cc03 | -16.6263 | -55.1934 | 2024-10-01 02:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 09761575-1897-3a57-9ca2-a70ed0864c82 | -16.6459 | -55.1908 | 2024-10-01 02:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| d9042c6e-25af-31c4-ae77-082ff7a2dc37 | -17.0898 | -56.7297 | 2024-10-01 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| d75bbbdd-ebe3-387a-bc34-0f57ed77925b | -17.0902 | -56.709 | 2024-10-01 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| f879269d-495f-3419-8da4-6cdf158c27f8 | -17.1095 | -56.7273 | 2024-10-01 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| ec1c0287-2b3d-3637-b35e-6f139dd02e56 | -17.1098 | -56.7066 | 2024-10-01 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| b83a9d3d-4383-38b5-82e2-33426fc69435 | -18.503 | -49.4506 | 2024-10-01 02:26:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f1e32566-ea7b-3c52-8261-b0f440a70699 | -18.5036 | -49.428 | 2024-10-01 02:26:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0530574a-0489-3b81-a5a8-56edc0e13e28 | -18.5231 | -49.4467 | 2024-10-01 02:26:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 34942847-d085-367b-b05e-f87f6fb3a750 | -18.5236 | -49.4241 | 2024-10-01 02:26:49 | GOES-16 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 562f5519-6d14-3ed3-89a3-c6c7df9add6d | -22.3498 | -49.3293 | 2024-10-01 02:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.6 |
| 2ab1d908-27da-30ce-8983-ac5096f9c9e5 | -22.37 | -49.3477 | 2024-10-01 02:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.2 |
| e3eba0c9-013a-3111-a896-119e8fca35da | -22.3707 | -49.3244 | 2024-10-01 02:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 367.2 |
| 67c2190a-52ec-3b8e-a630-e9247deba549 | -22.3713 | -49.3011 | 2024-10-01 02:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 161.1 |
| b4f9863d-929e-3c85-86c4-4488b28044fc | -22.3916 | -49.3194 | 2024-10-01 02:27:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| 00f1343d-3b3c-3227-bc5c-6dc49d346ea2 | -23.0793 | -45.3951 | 2024-10-01 02:27:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.3 |
| fcd01789-38c0-342f-9455-2bcd5642e01c | -3.0282 | -51.3345 | 2024-10-01 02:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 93479bec-0703-3a8a-af9d-4dd7a5859b8f | -5.9788 | -45.3621 | 2024-10-01 02:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 91f94742-e21e-3d05-b997-09ff006bf4d1 | -5.9786 | -45.3847 | 2024-10-01 02:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d39c3bdc-0f65-3bb7-9780-0a621e4467a0 | -11.2775 | -45.6427 | 2024-10-01 02:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 41ef276e-6a2b-3c71-b124-3ca32534b188 | -11.2584 | -45.6453 | 2024-10-01 02:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.4 |
| 0bc841ac-6ba2-3aad-a678-825b69ee0b1c | -11.258 | -45.6682 | 2024-10-01 02:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 300.1 |
| 81d5a525-bb8e-314b-9dc3-a7fd984c830b | -11.2591 | -43.3909 | 2024-10-01 02:36:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 93b2343e-9f29-3c4b-b5bb-2ce1d8c0b09f | -11.2771 | -45.6656 | 2024-10-01 02:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 22642de4-1c94-354c-8b27-2709756ba1da | -11.6743 | -64.9983 | 2024-10-01 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b18ab0ff-aa1a-366e-965a-98935b5db0d2 | -11.6556 | -64.9802 | 2024-10-01 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |


[Clique aqui para ver as próximas entradas](README32.md)
