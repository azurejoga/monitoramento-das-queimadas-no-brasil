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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a55cef60-7ce2-32fe-80ee-6042f0146895 | -9.82849 | -47.81765 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5296f3a-1890-37f1-9fde-52fc748e6398 | -15.03682 | -50.07718 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05ddb05c-3a75-3787-953e-6fa55dd59360 | -12.8654 | -48.02052 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f9b3027-5b6b-3d9a-842c-84e524947d8d | -7.71007 | -50.31769 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f5de72a-5af6-3891-a61b-e74bc4d62f62 | -11.44173 | -46.91863 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c77afd82-d150-339e-a830-98f5074b3757 | -7.70173 | -50.25434 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72cd995d-2f1b-3729-ae7f-32d60d5031c5 | -7.69344 | -48.7255 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5e73c198-de02-373a-95dc-cb27ae34223b | -10.97662 | -46.84865 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4e941a8-dbe0-3d44-a4f4-b2540a5a207e | -11.26788 | -45.31474 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0db4705f-1622-3f15-a209-c7c8ac823b99 | -11.61846 | -52.17787 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242ed5d7-21b3-384d-832b-bcbf0c07c9f5 | -11.64044 | -52.21248 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 244a9b43-38a9-366f-9f07-59c29fe708c0 | -14.90996 | -49.62584 | 2025-09-04 04:27:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdbb90ec-26ee-3977-9f1d-f6c26ec14d93 | -9.33372 | -55.21402 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d81eaf1d-5d4e-3657-8787-e0397d77bf39 | -14.295 | -53.09377 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 736c2397-6eb9-3b59-bdeb-8588656ace56 | -13.95901 | -53.97998 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28427be5-4629-3dba-9a66-030a469d84f6 | -9.98364 | -51.61992 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afd9a5d5-e677-39c8-b08c-0a024e86c601 | -10.95034 | -50.99749 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f926da48-7939-3168-b7da-32e2bbe4f21c | -12.9836 | -48.06911 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebf38be8-821a-3eab-b05c-924ff72bed4f | -11.67204 | -57.34244 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 36c01ec4-2fe2-3f60-b74a-d463411e10e7 | -14.73282 | -46.7465 | 2025-09-04 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 601a0a4b-e04f-362c-8fe6-9ad8653ab77f | -11.84782 | -47.54567 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d56af081-80c6-3e61-a24c-2ca519543387 | -8.07005 | -45.34453 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68f4c78c-b021-3bce-a518-2cea3f7197ec | -9.33471 | -55.20839 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d4088c81-bf3f-3074-999e-2b5629ad0241 | -13.73897 | -46.94164 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d156e1d9-b382-3e67-b644-8e453f67f1bc | -12.48096 | -48.08411 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9711acf4-aa37-3f64-ab13-309932ae26ea | -8.89481 | -45.81959 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1537cf9b-74b9-3b15-a831-de83770e1a64 | -7.7064 | -50.29428 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93bae2d6-f32d-3713-9580-06650100c998 | -11.64216 | -52.20256 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32e38607-af14-35e0-8d6b-a9649c1bbe15 | -11.58287 | -52.12243 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a0cad64-3852-3798-9cc0-38eaf8386131 | -8.25096 | -45.62877 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08b1d877-b8b5-39b8-81e5-6ee5378ade4a | -11.60655 | -47.78288 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fcebb64-b0b7-3a0c-a61f-684156b6b3ef | -7.25083 | -57.55093 | 2025-09-04 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f889ecf-85b6-3327-a1a8-1a7433d031dd | -13.86184 | -47.97742 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eeda4bf-0d84-325a-a0e3-dbd444bdde56 | -11.05368 | -45.15254 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| dc71f023-c09b-3043-bfe3-6465adfdf313 | -15.04117 | -50.05078 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bca7f16-9ce9-31a2-b807-64ee2bb04588 | -6.73918 | -58.74036 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 5f298d75-2e7d-3951-b5fa-b654fdacf76e | -9.95712 | -51.64777 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4baa9b2f-be13-3aff-9568-aecbf3568bf5 | -12.64442 | -56.99998 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e5fa443-8743-3526-92c0-16b21a7f7fd0 | -11.60325 | -47.78235 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e88aa168-91a6-3c67-adce-3be0e1af690b | -6.83597 | -59.36184 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ad4e8f74-5b53-3869-a098-40035bcb8be7 | -15.04758 | -50.0752 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96a964aa-cc51-3bd1-bbb6-49dfd4e85189 | -10.44162 | -50.26758 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08283a6a-9098-33ae-a785-1efc9adf4d83 | -7.69668 | -50.26203 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 46eee88e-2e30-3d7f-88e8-bb3b5a46566c | -9.43536 | -46.76516 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a35d62e6-7bc4-36c1-ac77-53a5242ee941 | -8.36851 | -52.54676 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92c32a6d-b2b5-3d47-8daa-c18a31f75ac7 | -9.47669 | -47.61021 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8ef33e0-4042-3097-bdb3-cd60e6b3ab01 | -8.09032 | -47.5771 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e483bfac-8156-3926-bd89-614cc86ae578 | -11.97738 | -45.79299 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 893cc37e-ae80-3d08-88a3-3d05972e7680 | -9.49412 | -57.8211 | 2025-09-04 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b930bdc3-2034-3838-ba9a-29d05a4a1627 | -14.81231 | -48.20608 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b0c2b1b-a335-3bc1-9f57-8b7df519b57a | -12.98304 | -48.07264 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63d0e535-3421-3b4d-84b4-5169e9a1c659 | -12.97085 | -54.77449 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8012c41f-29b0-3628-a7c5-d3671ae11e18 | -9.61806 | -47.03687 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 228e9f44-3b1b-3f76-913c-9e0f5437c632 | -12.89298 | -56.94782 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ca41348-fea9-389b-97a8-9ac0aaed3925 | -9.96965 | -51.63222 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50b4a026-35cc-31a9-877c-d4cba04d0b0e | -8.86202 | -47.92465 | 2025-09-04 04:27:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34384d8f-2cfe-3380-8391-93e2e796bb05 | -9.44149 | -46.79458 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c75a94ad-7a6f-3c26-8e34-f52959111fd5 | -13.44141 | -46.92857 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f8bc25a-3e89-3611-877e-cc212849b13a | -11.65057 | -54.52468 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b13ec59-c5c4-3ea5-938b-862d12a14489 | -14.82221 | -48.20771 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e463aebc-364b-31da-9644-b5a2187f98f7 | -15.04696 | -50.07896 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a392decd-9ad4-3115-b10e-066a14ed0950 | -8.05002 | -45.38557 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a93636bf-bd43-346f-88d5-0fd9140fcf81 | -10.44849 | -53.62196 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deed34d2-f3f4-313c-bd52-fe2259c0bd0d | -7.71814 | -50.31458 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9c8852cd-92f8-3907-832d-34ed9abc24db | -11.8854 | -50.6051 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa42ade9-e458-3328-868b-7edcae1e3c70 | -10.88625 | -55.74291 | 2025-09-04 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4be34bd2-6f38-3b38-9bb1-84859035b763 | -13.57197 | -48.13275 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29a16e18-af0b-3955-8902-4a74390430e8 | -9.41663 | -48.34995 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d1e9811-d3d6-3096-bb21-147fbc3fb223 | -7.71301 | -50.32273 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b8348b1d-5231-35c1-b24f-b95d019ecd89 | -9.71829 | -51.04904 | 2025-09-04 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3849e52-17dc-37ea-9ca3-fd4a040348ee | -6.75295 | -58.73797 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e3fa029f-3192-3c75-abff-b9b0a3e3cfe4 | -10.11339 | -54.79224 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d644d5c7-9728-3734-8101-e93d27b7c240 | -13.95414 | -53.98299 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51b303cb-fabc-3517-84a9-d5173715f6a4 | -8.03428 | -45.37589 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f5a52f80-7469-3a37-a229-d58bc98426eb | -12.45728 | -48.08383 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b0ceaeb-4524-3945-a085-cdfe04ea4bb0 | -10.05636 | -46.06902 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb34cac4-4664-3aad-b2f3-3bdab3c5676d | -9.32781 | -55.2187 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21dcdec0-0571-3275-8ea5-a30645af865d | -11.66998 | -57.35304 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b45cf12-f4e1-335e-b6fa-359933cbb36e | -13.63816 | -46.75422 | 2025-09-04 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9cd0662-5704-3dae-a062-2876f66ccf38 | -13.48936 | -51.80345 | 2025-09-04 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76146555-e559-3bb5-9c5a-f3b001a078f5 | -15.01231 | -50.0494 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3430ad64-2079-3640-be40-db87d062c21e | -8.89639 | -45.78699 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 944ea597-d209-3caf-b41f-8ec10c5a4c88 | -13.45313 | -46.94154 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d558fa9a-21a3-3c61-86b5-02e2d1923401 | -11.8659 | -51.46914 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be7d23fa-58c2-3147-ba72-db2f792aef90 | -13.85799 | -47.98042 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e5bd101-fbc7-3614-ae13-a0aa4c28fd10 | -8.07342 | -45.34502 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c1766d6-15ef-3f65-af39-0f1e28e1aea9 | -13.99263 | -49.5543 | 2025-09-04 04:27:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c8fb5f3-d14b-3a79-ae13-1cc610e6854e | -14.48242 | -53.21922 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae2f29f-79f2-3f71-bb47-1d5d66cf23e4 | -11.59994 | -47.78182 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e1806355-42c9-30fe-b14b-e45ecb0d5bc0 | -6.84346 | -59.15278 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 007f9e1f-6794-37b1-a041-945eff42c5ff | -10.12971 | -46.29939 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77628f72-9616-3b35-ba46-519e0efe7568 | -11.63828 | -52.20183 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 981dbb7f-06a9-3b18-9417-110cf2c1260a | -13.7462 | -46.93912 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37675c0d-4b19-3013-8a49-66000b8a431e | -10.10011 | -54.75798 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c763fc18-4d96-33a8-a36e-9812d18aec06 | -13.74956 | -46.93958 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a144e8a7-05a8-31dc-9232-133d36d6f8ef | -9.97349 | -51.6329 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff54fa1a-0132-3349-93dc-b368d10ad2fe | -12.90006 | -48.03697 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9be0f7e-85f8-318e-bf6a-a8bd82ffaa48 | -8.53274 | -51.32736 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2481c306-67b3-34de-8e3a-88a58e250dd2 | -10.00107 | -46.91241 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f425e251-57f7-30ae-a1af-b2e9a31650e2 | -9.81003 | -46.05618 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README47.md)
