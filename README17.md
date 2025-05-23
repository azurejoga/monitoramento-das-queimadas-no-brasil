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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4b26768-9a31-30f4-8f60-e8d18577b99f | -12.34612 | -49.98608 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab6f72d6-406a-3194-acab-9094106e2bc5 | -11.30096 | -53.98407 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15debb3a-b9d6-369d-b0ea-d7657f522e56 | -11.8109 | -57.35764 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 36dcae97-d397-3fe7-8801-2a61164a30a5 | -11.80318 | -57.36161 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ce9c5a6-e893-35ec-8e8d-23f7261f5505 | -12.33635 | -49.98574 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f6dc1f3-8cfc-341c-b845-0551f16926eb | -14.03175 | -55.13219 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acb2a202-a7a7-3c90-a916-ffa6c149b9d9 | -10.8206 | -56.9567 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92d02e24-c496-397d-8956-76a4d5f3d3a9 | -14.0707 | -53.38396 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be48257d-7c83-34ab-8e2f-8f32020fc7e7 | -14.03123 | -55.13609 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7455918e-e4dd-382d-aa8e-4b720d5890fc | -12.85146 | -47.39081 | 2025-05-23 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59d59c01-4578-38db-b686-66addb2846a3 | -11.80732 | -57.35808 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd8462cd-f0b2-37f4-aa9f-a84cf2962fa4 | -11.67088 | -54.93661 | 2025-05-23 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88aea944-d772-3493-95f6-054bb79e9165 | -10.68511 | -57.59964 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaf344b6-99e4-36f3-87e8-2ac4a1febe38 | -14.02605 | -55.14325 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e22898a-48ff-333b-b5b2-d823b6f80972 | -11.27133 | -52.47366 | 2025-05-23 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9b793e9-e6c4-3050-bc17-b3366747e8bf | -12.08491 | -47.34778 | 2025-05-23 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a2947cc-e364-38fe-a4e1-e32759764f3a | -13.79011 | -54.31392 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b81c2132-5792-39db-8b03-1942fd6b4667 | -9.41447 | -62.29483 | 2025-05-23 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96cd8324-b000-3377-b0bd-c480a4d9cf6d | -12.30268 | -52.49718 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8efa63af-5661-3de7-bb1d-92ea657c9e5b | -10.6945 | -59.098 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a7ecf63-cf0c-3903-92ea-1e4eb5e2c889 | -12.32754 | -49.99547 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0bf3af2c-e741-3cff-82ad-420fced31ea5 | -10.98888 | -59.15178 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3628224-6acf-3cd9-b3d6-baf55f6a62d4 | -14.04921 | -53.3802 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f2e19ce-5912-3338-abbf-4f1231bc16bd | -9.60292 | -57.91809 | 2025-05-23 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4f9d6c5-e17d-3df3-b912-8da160fd7a13 | -12.3409 | -49.98108 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b47b730a-1f0e-318b-98ac-318820bf995e | -13.98376 | -56.01867 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 941442cd-7cdf-3a9c-bba7-ecc1de9dda60 | -10.68165 | -57.5991 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c325b2b-7a5e-3033-b00d-2fc4a1bfe8f6 | -12.32182 | -49.99467 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9fc91129-e350-3284-8621-6226c0db502c | -11.81444 | -57.35818 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08da1c8f-246c-36b7-8502-e2d337b32347 | -11.65411 | -58.2642 | 2025-05-23 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa046470-1e84-3fdd-b69d-9ab5e4c370f3 | -12.84469 | -47.39008 | 2025-05-23 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74bcb953-1fc9-30bf-8943-33364331c9cd | -13.94383 | -54.48393 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8c58fd6-0e7d-3e18-91d2-49a82d7a323d | -12.53713 | -57.73668 | 2025-05-23 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23466b18-c7c8-34a1-8fbe-65589648dce7 | -13.25136 | -56.5447 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa7cbe5d-5cf0-3f5c-b5e7-faeb14a8bb56 | -13.15731 | -56.82216 | 2025-05-23 05:18:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c27f7994-5cc7-3641-a1e6-9176424563d1 | -10.98779 | -59.15886 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71e68129-eecd-39da-82a8-d49daa52bf17 | -12.42372 | -49.98503 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae2d38c0-3c9a-3c08-a921-b1cefa5aeb68 | -12.34041 | -49.98518 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81363c15-f83e-3e1c-ace1-511faec1d6aa | -12.06545 | -47.33885 | 2025-05-23 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54b18df9-a595-315e-beb3-f9935ffbba93 | -11.32663 | -58.62721 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f85878a8-f471-3b7f-ada8-08e6e2c7fd26 | -14.05516 | -53.37077 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 395d4af9-5828-34f5-90e0-a818ccb4dac9 | -9.49216 | -63.33315 | 2025-05-23 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47539aeb-33c5-31e3-a9c9-ae4da804f7fb | -10.3123 | -59.56947 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 978c28c3-1783-33da-8c0b-b63222419602 | -12.28296 | -57.26813 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5847d155-6517-387b-b5f8-a19a54b061b0 | -10.82356 | -56.96142 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feb3519d-f885-360a-883d-856cc68dbbe6 | -11.29666 | -53.98343 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c615a9c-3486-3fb5-9033-0b30ce07c925 | -9.24285 | -63.2941 | 2025-05-23 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6114f991-5c4e-38ec-9cea-7dab11526545 | -14.05049 | -53.37013 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00ea3c49-1d9d-3997-99c5-2386d21c4707 | -13.78687 | -54.30457 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6dbfa9f3-8600-3413-bebc-84c1f9e6c8cf | -12.34206 | -49.98667 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 234e61f3-587b-395c-a476-df659ae535e5 | -9.86152 | -60.31828 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d3f8c29-3913-367f-8b2f-993e918c3828 | -13.98837 | -56.01413 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c744ec03-f41b-3e69-a759-60b85c61a89c | -10.68452 | -57.60355 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccf2a2fd-5f8d-3fbc-961b-96f7f908173d | -12.38929 | -49.98081 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f9e0a4d-6f07-3506-b89b-044815d67814 | -14.0219 | -55.14264 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7689f1a-2790-323c-ab7e-8629a15bf659 | -11.57118 | -54.5675 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 668182c5-3def-319d-a4b7-4ec269c04dcd | -14.01931 | -55.13034 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daf9f52f-7326-3777-95c2-276c44aa7254 | -12.33992 | -49.98923 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6bd0899f-3d4d-37af-a467-2a41512a416d | -11.31093 | -54.02585 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b96cd1f-ed86-3074-bf34-b41f555ab03a | -14.04985 | -53.37517 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8180a73a-6daa-3545-a646-0d5ec91447ce | -12.47531 | -54.48226 | 2025-05-23 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d40ad4-be90-3384-bac4-040ab5f975a6 | -11.56012 | -47.4455 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5eddfe9-9cbd-3dbd-bdb1-54369e5c958b | -13.78575 | -54.31327 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a1da06e-85c5-3949-b962-b0582e04d213 | -9.42402 | -58.31297 | 2025-05-23 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70a3ef0-3c15-3e8b-a109-eab19472ff9b | -12.07149 | -47.34594 | 2025-05-23 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fa67a6b8-8496-394d-b0c6-13f4de6384d3 | -11.5661 | -47.45217 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88723d40-d3e9-37c6-be79-0d1f901a99dd | -13.161 | -56.82274 | 2025-05-23 05:18:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e87cdc0e-c993-3cb6-8fee-45cffed637a0 | -12.84751 | -47.38818 | 2025-05-23 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcbfbd6a-f9d7-32b6-8331-073876829e9a | -10.65206 | -59.28638 | 2025-05-23 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc3f3247-0519-3079-87a8-88dedd769889 | -13.98308 | -56.02375 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 92e0d375-f355-32fb-a706-15c4665c83b9 | -9.29338 | -57.55098 | 2025-05-23 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d53758e1-6b99-3313-a087-39b5859de642 | -13.98122 | -56.00793 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7793fe82-3654-38b1-9860-296c8baae8b8 | -13.16165 | -56.81824 | 2025-05-23 05:18:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ceeb8173-ab14-3a9b-8685-c3e9c64dd360 | -12.27938 | -57.26758 | 2025-05-23 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62d4b915-b33e-35f1-9e91-b2437dd5fd87 | -11.32904 | -54.24792 | 2025-05-23 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d05d9556-6a0d-3ad4-a50d-2351401c6606 | -10.82417 | -56.95728 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ecb5bda-aa43-3757-9834-d944d0237f8a | -10.68048 | -57.60689 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5672657-8a74-3fac-a6eb-f4d55aaf67c9 | -13.15795 | -56.81766 | 2025-05-23 05:18:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0de1f64d-16ee-3f45-9e9a-749cfd991c89 | -14.03538 | -55.13667 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d6f61b4-61a2-3384-ba0f-d35f9994f50a | -12.39548 | -49.97762 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8452b240-5bd6-3b10-970a-226a51094841 | -13.94816 | -54.48449 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6edfaa05-26f2-36f8-92d7-9ecefbc16cd6 | -10.68106 | -57.60298 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe6eabc4-26e2-3fe1-aad9-2cbb04cc185c | -9.4929 | -63.32874 | 2025-05-23 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ff78322-245a-31a1-9fdb-bcc41898f71a | -12.3359 | -49.98977 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e21b5630-27cc-32d9-b0d4-5ad13b305691 | -14.02242 | -55.13874 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10720cf1-2059-3ad7-a0ff-a6640ccf85e2 | -14.05388 | -53.38084 | 2025-05-23 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a002c2b2-0bee-322f-9087-dc4f22202f70 | -12.33682 | -49.98164 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2159f700-fcec-3bc1-9b4f-11f103fa9a92 | -10.9922 | -59.15229 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2ae58ac-0388-3e87-9e52-55e105d7c5dc | -11.57082 | -47.45059 | 2025-05-23 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5cd5f46-3d2b-3391-add6-d8af63ce8b29 | -12.3347 | -49.98428 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3bfd1f29-e65e-334d-8297-2879ae1d41b8 | -10.37032 | -57.5023 | 2025-05-23 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7321a55b-4e42-3804-bf37-33e0622c66aa | -9.36948 | -57.55882 | 2025-05-23 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 994a0ec4-3c69-3f5a-9f3c-71f356cdeaa0 | -12.39501 | -49.98167 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4489e86-f055-32c5-b33f-75c31b0f0616 | -13.18447 | -53.57102 | 2025-05-23 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d10f910b-ce3d-35ee-8ac1-946149ca220e | -14.01828 | -55.13813 | 2025-05-23 05:18:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df639df1-0baf-3412-8cc5-a7933339997d | -11.29292 | -53.97867 | 2025-05-23 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd076b0b-0ddc-3095-9031-59e11005974f | -10.98556 | -59.15126 | 2025-05-23 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60cf9bb4-65f1-3430-815b-4e5dfe525df4 | -12.29852 | -52.49107 | 2025-05-23 05:18:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a4620ca8-8a95-391b-a0cd-ea977b315f7e | -12.33421 | -49.98834 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 62926b5e-2fbb-3d93-9994-e36bed6fa5d2 | -12.4242 | -49.98105 | 2025-05-23 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README18.md)
