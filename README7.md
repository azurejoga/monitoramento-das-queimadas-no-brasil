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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c865015-4f8c-3d13-a3d0-135761b7e35f | -2.61711 | -49.23401 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc2c4253-d34e-367e-88fc-aecd9ca899b8 | -3.77524 | -43.98167 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c43617ee-6dbf-31eb-9d95-6a5d4f0ca630 | -2.94408 | -49.35052 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| caab5b35-aefc-3b84-a5b8-f72f2cdb669a | -1.97424 | -46.51164 | 2025-11-07 04:23:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 698e410d-5c3c-3482-9192-3376ba10e05f | -2.72749 | -47.3955 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8ed2253-151c-3629-a7af-9574df55d5ed | -2.94004 | -49.35241 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7119f122-9a04-355e-9e7a-a04a68d8d1cc | -3.31291 | -45.33069 | 2025-11-07 04:23:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dfa8f54-c71c-370c-a5b1-a2d8f5cdd10d | -3.09198 | -50.32439 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1703df29-4d35-3286-95e4-f7df7d4d59f5 | -2.94336 | -49.35511 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3a97ea4c-1b81-3436-a399-6fc4cae85591 | -4.01777 | -46.28177 | 2025-11-07 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4947f91c-707d-3699-9c89-2e15e139014f | -2.9707 | -41.7482 | 2025-11-07 04:23:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e2f5609-b64a-341a-84f2-fda3cc3b938c | -4.29769 | -45.88744 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a3d0ca8-21cb-38d1-9704-007a52af7fe2 | -3.17388 | -48.61076 | 2025-11-07 04:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ff6bba5-4de9-37ed-8b91-250ee73f0f7b | -2.67212 | -42.72715 | 2025-11-07 04:23:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79439f19-0745-383b-bf3c-feca91eb9d8f | -2.5871 | -45.35688 | 2025-11-07 04:23:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d727929f-5bcc-3425-aa42-ff23dad2f63d | -3.77805 | -43.98578 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58cec1de-f0ba-3257-ae27-aad24db8d7cd | -2.7287 | -47.38797 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 001a15cc-5d5c-3f87-848a-3c7319e14a07 | -2.62419 | -46.85161 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aa98f1e-e6ed-3ee1-8d09-5503abba0c9e | -2.79021 | -50.31172 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89805ec0-f09e-3fb2-9609-55b65d91f206 | -3.82429 | -45.34812 | 2025-11-07 04:23:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd28aaa2-9948-319c-a820-fd0710714a38 | -4.24738 | -45.62209 | 2025-11-07 04:23:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2f0fbb7-3af7-3ada-9099-b63715745984 | -4.8663 | -40.64211 | 2025-11-07 04:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b4ac77d-3d82-3b18-83e6-7bcc81373017 | -2.25826 | -47.87574 | 2025-11-07 04:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e9d2d01-9bc7-3bbd-9861-9eaa41dee98e | -3.17656 | -45.65727 | 2025-11-07 04:23:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b1f0ed3-5872-3709-9731-60f25e89644c | -2.62795 | -50.07597 | 2025-11-07 04:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 53590440-4ade-3ddd-a932-e6b83bb1300e | -2.82867 | -49.83065 | 2025-11-07 04:23:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ddb0ed-b038-35d7-91a4-b237d9a45084 | -3.43832 | -45.59682 | 2025-11-07 04:23:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b595306b-bd5c-35df-8a79-46fa01fcf144 | -4.30099 | -45.88795 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f40ab1c7-e918-3af0-b89f-df100150bc66 | -3.60165 | -43.51888 | 2025-11-07 04:23:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71303993-ac3b-31aa-afe7-60621c242493 | -3.52527 | -47.54858 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92ff6416-4b6a-3aa4-9342-121333a1d8dc | 3.46914 | -51.50806 | 2025-11-07 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c632a25-6ddd-39af-b1e3-349674bcfe40 | -3.17325 | -45.65676 | 2025-11-07 04:23:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10fc8092-13d9-3af4-bc17-ae298036ac00 | -2.85601 | -49.88566 | 2025-11-07 04:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3177681-c1b9-30e3-8f4b-7f893922722c | -0.89835 | -47.96354 | 2025-11-07 04:23:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 277fc703-43d2-3b3c-8f87-c45eaf38ec9b | -2.79423 | -50.31237 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20afa277-ab64-361b-a2f7-7f6a630ef7ed | -3.43502 | -45.59631 | 2025-11-07 04:23:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ca6f935-730b-3ccf-92d3-6a758d3e15da | -3.53975 | -49.43786 | 2025-11-07 04:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5522b464-7730-3929-b3bf-6f823596a6a8 | -3.37787 | -44.1725 | 2025-11-07 04:23:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8197cd9-4c40-3f0f-baf9-f89e28252663 | -2.77968 | -50.29195 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72056d5c-4137-3c3c-824d-5416a56c7e1b | -2.793 | -50.31213 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169a2c70-b9b7-3ea8-82e9-db6385898736 | -3.4275 | -45.35952 | 2025-11-07 04:23:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f4fba25-db3f-3fdd-9a23-34f260ba449b | -3.60093 | -49.44542 | 2025-11-07 04:23:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71d6716a-6513-3fcd-88ee-3dd402b81dd0 | -2.45025 | -44.14464 | 2025-11-07 04:23:00 | NOAA-21 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5a42d29-4332-302f-8e71-80f0904b75ae | -2.55093 | -48.39186 | 2025-11-07 04:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b37f4bf-ccb9-36a7-b98f-c4318a0a97e6 | -2.72809 | -47.39174 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e04cf41-4211-39b3-8512-bb24a846a7c8 | -4.86279 | -40.63788 | 2025-11-07 04:23:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de9adb62-76b7-30a8-89fa-592b927bfcc0 | -2.32354 | -45.64927 | 2025-11-07 04:23:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef483686-70e9-3118-bd2e-8c394e006de3 | -4.29715 | -45.89088 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8465f94a-cdc5-36ee-81f1-f49e4a5dd20b | -2.79365 | -50.3159 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8abfb38a-166e-39d8-aa0e-16682a7c06d1 | -3.29604 | -45.37374 | 2025-11-07 04:23:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9aa12b96-4813-3f30-8202-5abfbff1c53d | -3.56669 | -50.41647 | 2025-11-07 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cd0f0cd-61b9-3674-854a-82080870150b | -3.38122 | -44.17302 | 2025-11-07 04:23:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b23c7955-2c5d-36dd-898c-577ab9b8e403 | -3.77132 | -44.00682 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70ede1d9-31f5-3ef5-8742-7a594db426b3 | -1.44007 | -45.87974 | 2025-11-07 04:23:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 196ab4d7-3f2c-3ce5-b148-e8d0ff592201 | -4.28725 | -45.88934 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a3fd687a-1a5d-3097-a89a-9d144e816556 | -2.79244 | -50.31566 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8e7f5b-5a62-3321-9a8f-102f5c545585 | -4.90405 | -41.77876 | 2025-11-07 04:23:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d08fe426-4393-30bb-92d2-f1eb02755b7e | -3.17625 | -48.61169 | 2025-11-07 04:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c622809a-997b-3b44-8743-6d059147256e | -3.76851 | -44.00273 | 2025-11-07 04:23:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a2ae72d-c461-3576-94eb-9ae864085fdf | -4.46276 | -43.22977 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9d1eb51-789f-3f31-9865-08da77341fac | -3.21483 | -41.56939 | 2025-11-07 04:23:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f23238ca-2166-3ff1-909a-b10ae9b587e1 | -3.65054 | -38.85504 | 2025-11-07 04:23:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2b3848a-de91-3824-8313-41629bca883e | -3.17319 | -48.61495 | 2025-11-07 04:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc47a155-1203-319d-8a7f-f31abac13f23 | -1.79911 | -46.06449 | 2025-11-07 04:23:00 | NOAA-21 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b37d1a97-a056-398e-82fa-c79b73ea9750 | -4.64483 | -47.94971 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a713df86-acbc-36e2-89b7-004417bd54c4 | -9.24355 | -48.56183 | 2025-11-07 04:25:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cefd750-5932-3b57-9e3e-0fbf749316f0 | -5.75579 | -40.79239 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c5c4e853-1fae-3cb9-ad8f-725f4b40d822 | -7.03769 | -44.28679 | 2025-11-07 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28d0b95f-f99e-350c-b5cb-9054cfbff3d8 | -3.35382 | -53.22404 | 2025-11-07 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1fb3635a-c967-32b5-811c-44592d5a46ff | -6.57508 | -44.03097 | 2025-11-07 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2eb6e76b-c784-3c7a-8d68-db2edb47edf7 | -4.71558 | -46.431 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f295b488-0560-3d54-b469-9d9c9bee71d9 | -8.21337 | -43.81076 | 2025-11-07 04:25:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80aaed21-1a05-3089-aa2e-e7c01ed6490b | -4.11139 | -48.01633 | 2025-11-07 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ee62b9-339e-3d6e-944d-90b8f080a37f | -6.64629 | -43.61062 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c96470f-f064-3ff6-a7e8-79efbb4def5a | -5.42115 | -46.44682 | 2025-11-07 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6e50d47-adea-3d18-8d2f-642450952dfb | -4.71613 | -46.42752 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baf9e1a1-3c66-3ccb-a379-8530225d04de | -5.27386 | -47.16029 | 2025-11-07 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2a91627-818b-3a43-a0e8-c5e79bf08fc7 | -5.80384 | -44.51221 | 2025-11-07 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4b3110c-fafb-30f9-b82a-ccf29d082e0a | -7.7932 | -47.1147 | 2025-11-07 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb2ccf32-cba4-3952-972e-64a50061e4af | 2.56087 | -50.98024 | 2025-11-07 04:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5f3f2e5-cb5a-3de6-bd76-ab849c588634 | -6.59202 | -35.25719 | 2025-11-07 04:25:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6fec7a24-096e-3297-a8b6-49ed48e7ec63 | -4.68163 | -45.84592 | 2025-11-07 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 562da28d-b4fd-3f22-b95e-c7418902d0f8 | -7.79486 | -46.65125 | 2025-11-07 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b165567e-530f-30cb-8546-9b7aeeb8ab93 | -5.76332 | -40.7975 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32971441-5475-363d-a2c7-b92d95d1198b | -4.31649 | -55.84428 | 2025-11-07 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abace84d-b602-3cbf-8b15-4d9613a3a724 | -5.953 | -42.17415 | 2025-11-07 04:25:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dd14e6c0-cf37-3c30-acdf-af0a4928534b | -6.68388 | -43.55224 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f49c5992-0dbc-3879-81d7-f4ef8efc8130 | -5.09668 | -44.79917 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecd551d4-5484-338d-9199-8bc4b02cc6bc | -5.76788 | -40.79473 | 2025-11-07 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d7d78b93-a9ba-3adf-bcdb-4304afda7fe6 | -5.80439 | -44.50862 | 2025-11-07 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b51b308c-8ceb-3830-b938-7134953f73d3 | -5.39365 | -43.9352 | 2025-11-07 04:25:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0283cdc1-5397-3af4-8980-eecae1535d7f | -6.63375 | -39.50299 | 2025-11-07 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44b503f7-3e77-34f5-a4ab-d1635a5a6328 | -8.31654 | -42.20852 | 2025-11-07 04:25:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 166e69e7-2dd4-329e-9bd3-0914c65de485 | 0.98791 | -51.29659 | 2025-11-07 04:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 396ef305-9a85-3c6c-86ea-8aa554f24d1e | -4.6095 | -46.43589 | 2025-11-07 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67832a40-6631-302f-a1ab-a531435a45ef | -5.12942 | -45.63818 | 2025-11-07 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6001abb-ee3a-3f54-b26e-7662d58f0d7f | -5.09056 | -44.79461 | 2025-11-07 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bd60cac2-b1e2-3496-b9b8-401a89134812 | -9.72461 | -48.91131 | 2025-11-07 04:25:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab4f2670-a492-3735-8180-b667856dd895 | -4.31196 | -48.0789 | 2025-11-07 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e99854ec-a47b-3056-88fb-5875edb2fe10 | -7.0876 | -43.76555 | 2025-11-07 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
