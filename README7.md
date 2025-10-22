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
| fa2406b9-f89a-3720-a38e-aeeec96b20ef | -4.45586 | -43.24329 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| eff38e1b-f6b3-3231-bf64-983f9282d157 | -4.45237 | -43.24276 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0a3057ba-f6b9-3edb-92a2-068e3629252e | -4.4443 | -43.23866 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 479ea268-5ab5-38c5-88c4-af84b127a5fd | -5.15643 | -37.64473 | 2025-10-22 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 68dddb25-b59a-353e-af66-bc5e45a53807 | -7.639 | -42.17552 | 2025-10-22 04:25:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f492d77-634a-30ec-87f9-09e54c897e7b | -3.25133 | -50.134 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 668e5473-230b-3e3b-b683-f3fe285fb413 | -4.65671 | -48.69258 | 2025-10-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9038822-1d8d-386d-ad8a-ce8aa5325b6f | -3.96853 | -49.00871 | 2025-10-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f69289e0-150c-3048-99ab-097f50b5a6de | -7.22512 | -45.01413 | 2025-10-22 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee4d7261-0c8f-3f61-a955-cc797d6866ef | -3.24867 | -48.76944 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 950e6825-1030-38ba-b3dd-07b7706ff7d5 | -3.0269 | -49.46424 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e47bdf70-303f-313d-950b-eda15a236343 | -5.79232 | -47.71387 | 2025-10-22 04:25:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b85bfa0-b8eb-3036-bf0d-1ea162162e31 | -7.93135 | -46.01449 | 2025-10-22 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0de763a9-bd63-3e0e-b4f1-de8071c1c3d9 | -2.7756 | -48.58771 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77992198-4948-385d-ab2d-4da7b2ce4c96 | -7.07637 | -46.19877 | 2025-10-22 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 472484ad-cbad-37a5-a754-d611f6c7ae59 | -4.65607 | -48.6966 | 2025-10-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e649e1c-13d9-3ddc-8f89-cee9b0e61b92 | -5.41062 | -45.29155 | 2025-10-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4377bc4-735b-34c5-a919-ccbf396ebd79 | -3.24823 | -50.12837 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ffab774-c02c-3c87-b8b2-77ba038554d7 | -3.1534 | -50.16671 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd51dec7-4285-3c30-a14e-fa0808eaf73e | -7.66091 | -44.58838 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9af7b0f3-6fcb-35ed-8808-9d02b4b98933 | -4.44888 | -43.24223 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d77f1ca-0534-3320-a75c-8350a7c9544f | -4.91145 | -38.92634 | 2025-10-22 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 05e04f41-4bda-3119-b2ec-b31d3f1b01b2 | -2.92666 | -48.30102 | 2025-10-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cf82f086-4d58-34fe-a5f3-eb928d335396 | -3.82069 | -47.41216 | 2025-10-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c520ac41-a756-3f03-9bd8-37131770056f | -3.8996 | -47.33088 | 2025-10-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf1bc2fa-d91f-3ad4-93a3-4c2a8387548d | -3.32876 | -50.22863 | 2025-10-22 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ffef98d-6bb1-34db-b524-3b4e9c5cf09f | -2.02359 | -56.88143 | 2025-10-22 04:25:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efa21cef-c6c2-32a9-88b1-aed095367636 | -2.96345 | -48.58986 | 2025-10-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5718faa-ad40-3459-8ecd-8695730694c6 | -3.02081 | -49.45378 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cff94cb-8bf6-3330-8a6c-983370fb2b0f | -9.90115 | -49.86224 | 2025-10-22 04:25:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6119cf72-8882-3b7b-b533-87f05c38898a | -7.07691 | -46.19533 | 2025-10-22 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4f0037d-205f-3c3d-99a2-b972e4975032 | -7.94061 | -44.84912 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 372628ec-f57e-3f38-b318-9be36eace08f | -7.94455 | -44.84599 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9841c203-a266-397a-8076-bb09c8e6dcbf | -7.71352 | -46.60414 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ec414f9-087a-32cf-b1a8-d56e2e8df59c | -3.02672 | -49.46762 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ba6fe76-7632-324d-bcd1-d95ce1131530 | -9.83468 | -44.27016 | 2025-10-22 04:25:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af1818d1-b935-3d4a-a960-de2d6d87aa60 | -5.41116 | -45.28807 | 2025-10-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c89bb96-6db4-3dad-89dd-23982b4fabac | -3.04115 | -49.52176 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cbad86c-16a2-3ccd-a037-d837da809893 | -3.25183 | -50.13084 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6e801d2-83d7-3966-8e16-b51b3579f54e | -4.3952 | -43.30243 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 290b2c26-c760-32c0-9aac-9b63cf407328 | -8.96312 | -48.65164 | 2025-10-22 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f06258e-6613-3418-b5fa-57d15001c2af | -3.25104 | -50.13584 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1bfbdfae-918b-303b-ae29-251202d47692 | -3.25525 | -50.1346 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e399049-060d-34dc-983d-0b6c5bbb3599 | -3.14946 | -50.16612 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 506df123-240a-3b55-88a3-caeec3dcfa57 | -7.93189 | -46.01101 | 2025-10-22 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 600e00db-761c-38ba-881c-b7274603d899 | -4.90916 | -37.20072 | 2025-10-22 04:25:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7c68caa6-3fa1-3351-afe6-18cee42a7f52 | -7.32667 | -45.28498 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37283e9a-2cdf-300f-8333-27dee45e81b8 | -2.876 | -54.86276 | 2025-10-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 274340bc-68e5-3ec5-9b93-7fd5ef1b2106 | -3.25215 | -50.129 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c90ed64c-50bc-3b61-9712-313dd0ff6527 | -7.74429 | -46.56303 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e5baba3-a798-362f-a938-8bb0b9909e73 | -8.23106 | -45.75036 | 2025-10-22 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 108654a9-f884-3c4f-931e-3e0e0eea0613 | -10.24996 | -48.47044 | 2025-10-22 04:25:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0903e719-3750-394c-a4aa-4df180e64858 | -4.90687 | -38.92565 | 2025-10-22 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 848265eb-7a42-32ef-8f1d-ad4c5d064557 | -7.49344 | -47.03075 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c321c88-eb09-37d6-9262-fc10e2b8e3a4 | -7.93465 | -46.01501 | 2025-10-22 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f599490-3fa1-3769-8a71-3c136875e127 | -3.02008 | -49.4584 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afc34aec-da9d-3f5d-9f0a-90c4ee0d3fef | -6.32385 | -41.88325 | 2025-10-22 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1191a9c6-04a3-3c82-ae38-90c64a20a89b | -3.0253 | -49.44978 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb18eae4-0853-3382-8281-6743b76934ba | -5.42057 | -47.11542 | 2025-10-22 04:25:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa76ed48-e0ad-3823-b46f-ca7fdf737888 | -8.77642 | -45.78543 | 2025-10-22 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b76c9621-6b88-30b9-a679-35bfa6abb726 | -4.39054 | -43.30959 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 500efbc3-79d4-3d79-9b8a-6cdeccfe35c5 | -6.35302 | -47.50378 | 2025-10-22 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc590106-aec3-3d2b-a8de-51a47d509634 | -3.14551 | -50.16554 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5419db1d-9777-3064-8c18-cb5aefe1de40 | -3.02748 | -49.463 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f67c2ed6-d1f7-3dcd-9f07-1c6c388b8346 | -3.02312 | -49.46363 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2472fe92-f942-32c4-8050-bf4017ca6cc0 | -3.56717 | -49.4843 | 2025-10-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 995ae191-7ff5-30ba-8197-743d150582a0 | -6.53071 | -41.43258 | 2025-10-22 04:25:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 080d202f-4914-3f07-8a6e-738762cfcb76 | -7.13343 | -46.17939 | 2025-10-22 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 485023c5-4007-383a-b262-c62018340683 | -4.44946 | -43.23833 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16280641-78ad-3ae1-8371-62fde6a3ab9f | -3.03125 | -49.4636 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3c3fb67-2b0f-3c30-9ab7-696da58f7918 | -7.16069 | -44.9934 | 2025-10-22 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cacaa213-19b4-3862-bc4e-e46f67575c24 | -7.08104 | -44.11058 | 2025-10-22 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 677297a4-f4e4-3729-923d-2eb1dcf7dbbd | -2.87058 | -54.86176 | 2025-10-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca812312-cba5-375e-b4ce-71d5aa92aeca | -6.33808 | -43.51141 | 2025-10-22 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e93ab84-1a75-3c1c-b7d4-0e0cbd4d82eb | -5.36063 | -48.10817 | 2025-10-22 04:25:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6c4b57e-8846-38a2-bab5-44a3d96cc63f | -4.60815 | -46.59227 | 2025-10-22 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c3c170-fe75-3b89-a2d0-4e65644ff47b | -6.81336 | -45.30697 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c95c0420-c49b-371e-9906-bc7dbe0e0543 | -3.33797 | -50.74817 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e7415ef-8317-3092-bc5c-bcfb7f526ca9 | -5.97727 | -46.60719 | 2025-10-22 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2b97a53-5e51-3f64-8f07-760f21c5cea9 | -8.22828 | -45.74633 | 2025-10-22 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac5051e8-9142-36fa-9f47-48320c3eb468 | -4.90589 | -37.20128 | 2025-10-22 04:25:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bda8bbe5-53e4-3209-a2f5-368a298d0cca | -9.56406 | -43.01977 | 2025-10-22 04:25:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70289a55-61c4-37f9-a6be-04beba4bf9ba | -8.1966 | -49.67369 | 2025-10-22 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31d64f52-a1db-3242-87a3-88ca4a887e9d | -4.90619 | -38.93034 | 2025-10-22 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1b0a47a-38fe-33ce-800a-96d3c17ebb07 | -4.44779 | -43.2392 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47555612-3e0c-3dcc-be3b-97a7af04570e | -3.25575 | -50.13146 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b43127e8-f0ba-386a-b770-2d529cfbc081 | -7.35251 | -44.76735 | 2025-10-22 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 004b0ad2-ba11-34fc-9479-58bf6e4265ce | -5.29978 | -35.97917 | 2025-10-22 04:25:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bd03d0f-f465-365c-8006-8ffba185f583 | -7.93411 | -46.01849 | 2025-10-22 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 354d2d60-d5a7-3398-a28b-a2c2614d8eee | -4.69257 | -42.9464 | 2025-10-22 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd507a17-f202-3970-adfb-edf9e6146f79 | -3.94162 | -48.08368 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0671a3d-4eb2-3c19-807c-756bf5459a33 | -3.03067 | -49.46485 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bbc0614-7cfd-306d-895b-43f80f26faf7 | -6.81777 | -45.3005 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6786f986-69e2-3bd5-80ca-7651739e152e | -3.66926 | -50.2869 | 2025-10-22 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2b9f9b8-60e1-364a-ba75-2249cd0eddb2 | -6.33879 | -47.37773 | 2025-10-22 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f9f62af-efcf-37c4-8bf8-952b4d9cc763 | -4.22774 | -47.21194 | 2025-10-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45fda3f7-3d77-3a82-8023-d6d4934883f9 | -3.11727 | -49.21775 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5d8ecd-b0cc-3757-8918-33dbaa41c7b9 | -3.56342 | -49.4837 | 2025-10-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 223f3a3c-53c3-31fa-a795-b85e22d19abb | -3.94448 | -48.08808 | 2025-10-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 895106c2-780b-3838-8d11-eda1afb3b848 | -9.83411 | -44.27068 | 2025-10-22 04:25:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
