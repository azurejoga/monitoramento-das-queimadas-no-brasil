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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0cbc677-2cbf-3ea6-be79-56b146a639d9 | -11.51207 | -65.11717 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cd5b7aa-2786-3381-b2a4-ad61a670e7c2 | -11.51146 | -65.12125 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bdcb2c1-6d35-3c52-8467-597b7706edf9 | -11.50078 | -65.11962 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5408b408-5a8a-366a-9b5f-380a78e47c76 | -11.49426 | -65.11447 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82c72aed-1d92-3fb8-8836-ffd902a6b4c5 | -11.49366 | -65.11855 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86ad88eb-2fbf-3f07-bef1-dacdd1d21fe5 | -11.4907 | -65.11392 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36db62e0-f0eb-336b-9a60-5cab5bfae893 | -11.4901 | -65.118 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c057229-107b-3593-af25-a88d0fa61386 | -11.48894 | -65.10114 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aabc34c-f89b-3791-9ed5-988cb729a943 | -11.48834 | -65.10522 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a082fd7-8adf-3e06-aa15-3e4d76d5ee2a | -11.48774 | -65.1093 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efccb25a-c075-3a8e-9f9a-6f84b4da47e3 | -11.48714 | -65.11338 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 612fdb30-be09-3d42-85d4-a88254bfc7b5 | -11.48654 | -65.11747 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efaa7ff0-4dfb-3e92-90b7-5f0f541252b2 | -11.48477 | -65.10468 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51d85833-4fcb-3020-b331-141a3442d3d1 | -10.8859 | -69.39149 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c74cc848-1054-30a3-a5c2-0b34ca808956 | -10.88287 | -69.40996 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14948926-6973-3bae-9820-02688b60c061 | -10.8795 | -69.41008 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3fb5a4f-a780-332a-8d6a-d954778f5e12 | -10.87947 | -69.40939 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048ea3f0-eb7e-3d5c-a975-cac4f3e6a118 | -10.87928 | -69.73158 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97127641-bf24-30f7-9f07-c9c058e8b9b8 | -10.87584 | -69.731 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a2a4c5a-0ace-3972-8570-c16092da3fbd | -10.86912 | -69.43114 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e07c5bb9-400b-35f1-8a30-5ede378e160e | -10.8033 | -69.53458 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95ce22ee-24c0-33a5-b790-58bc65522a2d | -10.68825 | -69.35974 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07ead98-3d09-3eff-837b-36b6fbced8cc | -10.68052 | -69.44971 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bed6b03-91db-3b9c-b550-c2307b03885f | -10.6343 | -69.30598 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 574b16e9-5da1-376e-802c-4c64c4c4edf8 | -10.5711 | -69.32955 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27616f03-1dbf-3b82-9548-82ee37720987 | -10.51445 | -69.35399 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c5501be-8165-3c5f-8474-a3fbdabbeda9 | -10.51104 | -69.35342 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dad26ae3-17c8-3792-a454-d109700603c9 | -10.48607 | -69.22821 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9e6fe4e2-a803-3860-9120-322fa792ca19 | -10.47847 | -69.25336 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ecaf52-9deb-3bb8-a51c-2f2a77894815 | -10.47014 | -69.21854 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9192aef-95fd-3acd-8835-e91d8d2f57ec | -10.46716 | -69.36509 | 2024-10-16 05:50:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f62f18a9-20b9-3a92-bb02-07cbc2340b47 | -10.46423 | -69.25532 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83212213-05ac-3666-806e-be30ca18a7ee | -10.89194 | -69.35467 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 212de6a2-4bcd-36fb-a600-b95b4440b5e7 | -10.8893 | -69.39207 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b40cec55-b3ea-3e8c-887a-4763ac3a9e60 | -10.88529 | -69.3952 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c01e2ac1-fd17-31b2-ba5e-82cd2dc0145a | -10.87872 | -69.2851 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbc65e9b-7f63-358a-a620-40ee329f66e9 | -10.86035 | -69.58952 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5218d3f-f55b-3943-8136-7d51e707fef1 | -10.7503 | -69.40805 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac47217b-b9de-31a2-8b18-e200e9602f17 | -10.71479 | -69.49747 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e652b549-1078-38ab-930b-aae9ab19976d | -10.71082 | -69.43574 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d05b1203-ef79-3b44-9050-05467178a8eb | -10.68886 | -69.35606 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b634680d-ecca-376d-8fde-e4d75d29848b | -10.68358 | -69.53819 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2656474f-b367-3324-9831-9671719c6ffd | -10.67843 | -69.37707 | 2024-10-16 05:50:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4de288ce-2b0b-38f9-82f5-a4583c08502e | -10.90555 | -69.63554 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca85851b-7ecc-38a0-95f8-2ee5ed897031 | -10.90494 | -69.63929 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 210aa357-3241-3b17-adb5-8cb3222904c0 | -10.90152 | -69.63871 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 798ef08f-1ab7-3cf0-876a-41500d7e9390 | -10.90213 | -69.63496 | 2024-10-16 05:50:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0cf9c845-1dfe-360a-81be-57287daec517 | -20.99718 | -55.23848 | 2024-10-16 05:53:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 824ba723-7015-3e29-ac20-26f10226d533 | -20.99717 | -55.23235 | 2024-10-16 05:53:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25c8e1e7-0832-3add-8506-bda4595246e3 | -20.9966 | -55.24028 | 2024-10-16 05:53:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22877574-2c1b-3f62-bdb0-b6d670bad358 | -20.98925 | -55.23968 | 2024-10-16 05:53:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3b3884c-f20a-3922-b484-b14bb35f0b4b | 1.0016 | -52.2164 | 2024-10-16 05:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 688cf065-589b-3105-a0aa-a61b23c98595 | 1.01064 | -52.22367 | 2024-10-16 05:55:00 | AQUA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6b98ee48-98eb-30ab-8374-1dd25811c2db | 1.00923 | -52.21424 | 2024-10-16 05:55:00 | AQUA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 91de9752-7b93-36c2-8566-693b898e6612 | -3.28733 | -47.12546 | 2024-10-16 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 24e3ea11-11eb-3f8d-8547-5907c7c34da0 | -3.28272 | -47.11985 | 2024-10-16 05:57:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a73734a0-0901-3225-b244-b157cdfcc75f | -2.52954 | -47.21659 | 2024-10-16 05:57:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4f91772d-3071-316b-8810-e550ca4af771 | -3.96347 | -46.40934 | 2024-10-16 05:57:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 3457f197-f1e0-3056-8a54-937b3d91b299 | -3.96199 | -46.41406 | 2024-10-16 05:57:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 24044331-b497-3882-bc6b-f1150d730224 | -3.95928 | -46.43831 | 2024-10-16 05:57:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 11c11c2c-fc14-33a8-a64d-a70edbd87da5 | -3.95811 | -46.4424 | 2024-10-16 05:57:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 53e6b5ad-296d-3e50-9fc4-e2624bd59489 | -3.22425 | -48.90759 | 2024-10-16 05:57:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c60079d4-5d59-3df9-b9dc-74a055801223 | -3.22179 | -48.92525 | 2024-10-16 05:57:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b4c05622-4718-3f3a-afa4-e90d466fa3d2 | -3.21749 | -48.91946 | 2024-10-16 05:57:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f8af7ecb-5635-3a5f-9128-5d47fbc26c5f | -2.95802 | -48.00357 | 2024-10-16 05:57:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| df7f5621-c355-3ac4-b87e-146af3b1b60a | -3.07662 | -50.35218 | 2024-10-16 05:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 72c98d51-2746-35b0-85f7-e1e6d7835a8d | -3.07464 | -50.36577 | 2024-10-16 05:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e824d547-3841-3113-a020-7d75b8b44108 | -2.61843 | -49.07853 | 2024-10-16 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 410df239-85ba-32c7-92ee-d88ddffa6bb3 | -2.616 | -49.09523 | 2024-10-16 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 6a1733f5-c37b-34d3-b01b-27c1a9e6aee0 | -2.60169 | -49.11009 | 2024-10-16 05:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 66030213-f3f8-33c9-a2c9-7b485a83556f | -4.41807 | -50.68967 | 2024-10-16 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| badd3ef8-5189-3388-aa8f-0b6451c83369 | -4.39021 | -49.6725 | 2024-10-16 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e978c4f-78ca-3f4e-8c22-514ad26a7716 | -3.98108 | -50.71263 | 2024-10-16 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1f5aff95-22d3-3bc8-ac41-a8f4627a09f0 | -3.97805 | -50.70536 | 2024-10-16 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ebed8573-4ba7-32c3-88fd-75201b331e6a | -3.58578 | -50.5711 | 2024-10-16 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 04163b55-50e4-39e9-b587-7f044350a69f | -3.50932 | -52.15802 | 2024-10-16 05:57:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| abfa9d4c-cb5d-37ac-b999-a57e6da764fe | -3.28864 | -50.93232 | 2024-10-16 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5e84aa5a-c84d-3392-92a8-6ade9c04b740 | -3.27823 | -50.93085 | 2024-10-16 05:57:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| dd542979-cebc-3211-b7b0-e2c5312d4962 | -3.06836 | -51.24095 | 2024-10-16 05:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 23ad6629-d99e-3e0e-b67b-c27f05fafb1e | -2.88184 | -51.67863 | 2024-10-16 05:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| eaf08a5f-57a4-33cb-b859-3d544b8a9c05 | -4.35659 | -50.96388 | 2024-10-16 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 01d75d74-2ab4-3502-9a4e-f7adffc6a3eb | -4.35472 | -50.97689 | 2024-10-16 05:57:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c2aa7e16-c345-3b84-a7e0-c5ad69f7d39e | -3.77958 | -51.34971 | 2024-10-16 05:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| facd089b-f70b-33a5-b48c-e6a381790f91 | -2.09004 | -53.40664 | 2024-10-16 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0961b362-85eb-3666-9ac7-b6476ccc0034 | -3.12253 | -54.22126 | 2024-10-16 05:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 38280ee6-6182-3e1b-ac04-7ff2b1b7f488 | -3.12121 | -54.23009 | 2024-10-16 05:57:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 727fd74b-828d-3f8f-964f-be0d33918809 | -3.11285 | -53.73064 | 2024-10-16 05:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2fbb6785-8a56-346a-ad93-fd31892cdace | -3.11151 | -53.73965 | 2024-10-16 05:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 19ca5f1e-1fd2-375d-917e-9f8506d6056e | -2.39374 | -53.72358 | 2024-10-16 05:57:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ddcbc567-d45f-3eaf-b983-f8b3baec7a0f | -3.62827 | -54.66511 | 2024-10-16 05:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe7aecc4-3fec-3d0e-ad4d-565aebc8afe3 | -12.05232 | -46.70805 | 2024-10-16 05:59:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4405e060-d87e-3dbf-9f8b-c48ee6799dcb | -15.91356 | -56.30491 | 2024-10-16 05:59:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a6f66a25-709d-3327-a79e-c94b30865e47 | -21.00203 | -55.23405 | 2024-10-16 06:01:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a1d3c918-999b-38dd-a68a-aa12f38e9e5e | -20.99377 | -55.22611 | 2024-10-16 06:01:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b10ae3d4-eed8-36c7-9c98-2d21ebc17568 | -20.99215 | -55.23841 | 2024-10-16 06:01:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 67f10ab7-7252-3d50-8201-788f0194b26a | -20.99198 | -55.2326 | 2024-10-16 06:01:00 | AQUA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| a4b23173-19f9-35d4-ae46-235655fab979 | -19.60384 | -56.97414 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.3 |
| e19f86df-c0a3-36df-8bd5-a058d944d20b | -19.60245 | -56.98395 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.1 |
| a1f81064-86a5-39c4-9e78-7b9b4bdacb94 | -19.60106 | -56.99375 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| c46e3839-50a6-3b7b-89d6-cd0f128db47d | -19.59615 | -56.96293 | 2024-10-16 06:01:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |


[Clique aqui para ver as próximas entradas](README72.md)
