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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fcfa447-f49e-3faf-b9d7-d315e1ed93e7 | -2.84731 | -54.09521 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83c6d982-dbb2-3819-83f3-7b685d767e94 | -2.44302 | -46.53988 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 209d2c62-0e52-3f6d-931c-274adf6a2f2f | -3.23161 | -54.25689 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 592639ac-a9b0-3449-ba01-058fc653fceb | -1.26843 | -51.59619 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a16ac14b-9399-3c03-9bae-d78a84580c56 | -2.61229 | -46.19567 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4812c564-b775-36bf-923e-6afacfce219f | -3.52161 | -53.79455 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4e62941-7495-3d33-91f2-908f20a46f96 | -3.31482 | -47.02036 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed536377-4744-3272-ba8a-00abd2822b00 | -2.21457 | -50.82281 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2958f4db-d7b4-315c-922c-bb5944260dc6 | -2.56444 | -54.07131 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 634685ca-bf3a-3b41-88aa-9664a18e646f | -3.82953 | -52.25383 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50f80917-2822-3d8f-830d-8f1f83b50935 | -0.81435 | -51.60225 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285ac720-0f7b-395e-be31-9cb903fcdcfa | -1.69852 | -50.20634 | 2024-11-22 04:36:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17e6149d-a067-355a-9d88-1cd7b95bc7ed | -3.06382 | -53.28976 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05455153-25ec-3ba4-905e-645c38f098c6 | -4.06438 | -46.83972 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dcf5db6-8b6c-3549-8c44-9e226ccd3656 | -3.2371 | -54.25753 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dfdd1dc3-50e7-3b0d-afd8-e5288483cf4e | -2.71713 | -48.89001 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3b0d7a5-8f0f-3da1-b76f-f7fb85268d58 | -2.77536 | -48.64919 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7adfc4af-4a76-3783-8b27-e9ddaa44de95 | -1.78944 | -53.62973 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f434cc-2846-30e1-9b05-924bf06116e2 | -4.01903 | -43.98744 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c9bda05-aa1a-36a4-b67c-a031267c37d2 | 0.43958 | -50.77459 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45080b17-9c99-3607-90a8-f4b837a07261 | -2.62181 | -48.17791 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 598237fc-a7c4-3cb2-ab7e-603a34eac2fe | -2.14105 | -50.49032 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5d5ed94-0244-3cb5-ae56-3a556197e1b8 | -1.63499 | -52.39925 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bc76c0d-3481-3557-aa5a-66b9d5be9b13 | -4.70697 | -45.8144 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc527b5-25c3-3d90-abe2-28814269f1bb | -0.16718 | -51.62639 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ccffb16-a1d0-3076-aa6b-f30fee8a4c60 | -4.28356 | -48.21784 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1b64b0a-b07f-35ee-8894-661810901042 | -2.44359 | -46.53617 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf2c6b8-3aae-3adc-ad4b-0a7ba8c807a5 | -0.94865 | -51.72129 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21e73e4b-1feb-3202-8c00-e81f71571c59 | -3.23677 | -54.2337 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 903282c2-7eb1-32b6-84d8-67f5ed13efa4 | -3.25156 | -54.24781 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c7024c2a-12f3-320c-87a8-df4008b912ba | -0.26808 | -51.57831 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 035ee5ee-04c2-3688-a922-d2b40a11d5a0 | -2.63423 | -46.21471 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 584fcc38-3e19-36ea-9fac-b35062ba7ee1 | -3.67224 | -54.27503 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e035ca04-fd74-3f27-8e1c-083b0fc8c0be | -1.36605 | -51.38016 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae1601b3-eee1-3ce4-a646-494f6ec5d07a | -3.75403 | -44.56934 | 2024-11-22 04:36:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a0248081-0f4b-3801-850c-021143ec882c | -1.19574 | -51.77035 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87522456-d29b-34d7-b399-6e582caf811f | -1.59303 | -53.81075 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 4d516b46-e1ba-304b-829c-f5752a0ae408 | -2.78071 | -51.72113 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ea1ca6-f9ff-3e78-84ad-353b16842d99 | -2.44644 | -46.54041 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf1095eb-1568-32ad-80ad-ec76822875f3 | -3.28523 | -53.83998 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f19c729b-f1f0-32df-844c-b11bea0d8519 | -2.84965 | -54.0034 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675dbe41-5f1a-3c22-87d4-de6839805efd | -1.74405 | -52.3952 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 346a16ac-c720-315c-bbb8-7b3bc98dbb07 | -3.31538 | -47.01672 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4ddf0390-05db-3354-bfc1-72f56448e7cc | -1.4944 | -49.6819 | 2024-11-22 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34532d70-afd5-320f-8080-ef37b0e784b7 | -1.33126 | -47.95894 | 2024-11-22 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e5685ca-7efc-3fbd-9f50-91ecbbaa578d | -2.72583 | -46.09407 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cef31d11-a3b4-3694-b13d-470b9d58eb95 | -3.27994 | -53.82102 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 39aba5f0-a23e-3282-8650-6cf68fd69a97 | -2.56007 | -46.55397 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c462b6e3-42ae-392b-8e25-03c7090b3a25 | -1.24095 | -51.7465 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 262a5971-96f9-3de8-b6dd-e764dcfcff29 | -2.22449 | -48.37315 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d2a61bf-6b64-369d-9f75-ae2afe2382be | -4.25801 | -46.81031 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64424634-a914-30a5-9402-bdc23d3c4619 | -0.26644 | -51.56468 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f91ed67d-12d6-375e-829a-07619c015673 | -3.60755 | -51.314 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e7d39b4-ad3c-3242-ac05-d57e44d57459 | -2.55495 | -46.54175 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eff1d774-c556-35ba-b4bb-f8795f35a087 | -2.57425 | -47.9833 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d5de9f1-dbf9-3914-8ad7-e691a14f8aa6 | -1.19323 | -53.68158 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12df2425-ca69-36a6-925c-ef3b90c10199 | -1.12087 | -53.40425 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c1a6da94-23af-3205-9d72-f6e3be23bcdf | -1.62898 | -52.41256 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26b737f8-9461-37d7-b3bc-1459cf0e74f1 | -3.33757 | -53.33445 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 88a78694-58f5-3404-9693-2df5ef238ac7 | -4.53671 | -46.61904 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61b3e7e3-8fcd-3389-aa19-8ae62441a893 | -1.43414 | -52.67282 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fcbb8be-3757-30b2-b459-dfd160339fcf | -3.24281 | -48.00955 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| def1bb52-00fe-3a3d-b8ef-211fa23e0a79 | -1.77187 | -53.6082 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8cc6957-be8f-36c2-b7bd-2b7a619ea34b | -3.48327 | -42.2995 | 2024-11-22 04:36:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 098ca58a-7467-35dd-b25f-133f45fce5c9 | -2.26565 | -50.45599 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc0b7f16-ce82-36e8-82a7-c03e97eeaf49 | -3.65999 | -51.57332 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d5618e8-305c-3855-83cf-b173a8853a0a | -2.76546 | -54.06264 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78e1d52f-c3b1-39c0-b0b2-f2531804465c | -3.2806 | -53.84295 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ee96bd0-fbe5-32bf-b6ba-48d743981666 | -3.50212 | -53.81295 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 594bff19-b339-3081-bf41-de16a3869b57 | -2.69386 | -46.06929 | 2024-11-22 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2aa5fdb-0c47-309d-ace1-2b9304de69bb | -3.31199 | -47.0162 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c54b898e-4ac1-3c50-aca0-18c1d2b3369e | -6.27025 | -44.5477 | 2024-11-22 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f3a1536a-f2ef-3971-8be5-d01e951a8f25 | -1.13558 | -51.67863 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 985f48ab-74b3-3b1c-b5b1-5653a1c46008 | -3.85541 | -52.3508 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4181b30e-4be7-3fa8-83aa-66bb073dc754 | -1.22985 | -51.79357 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac86d1ec-c51f-3baa-83b7-01201f0b78a6 | -2.38266 | -50.33804 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ec8f7e5-f388-39d8-a823-3c5e64525518 | -3.96651 | -54.13901 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 852f3b9b-cae0-3b5e-8c45-ab86c5176c04 | -3.23614 | -54.23751 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7527e1df-d265-34b1-982b-f0eba7531b34 | -2.85867 | -53.97436 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9a2155f-63cf-320b-8647-835f8e48a7af | -2.50641 | -48.99776 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52626e0d-17c1-3e5c-8df1-c430182bc709 | -2.46043 | -49.18174 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10653831-f7c1-372e-84e5-0133a85c5143 | -2.45323 | -53.70047 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8156eac1-06db-3908-a878-6b36828b8469 | -1.2596 | -53.37125 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85171168-c485-3d12-a9b7-f6ad9b1d4a03 | -1.27002 | -52.69821 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614be509-2b18-3648-aa91-774da8a344f1 | -3.2461 | -54.25491 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8dfc5960-72e3-31c2-a7a8-b3da693f7738 | -2.05552 | -48.2585 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7f77d3b-6ae7-3507-8fb4-a99187967f28 | -1.83797 | -52.17453 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67ba6005-e682-3114-b227-492cff74ff2b | -0.93095 | -51.72035 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca3a4b01-7ee9-3069-bddf-ba1d4d36e66b | -2.55701 | -47.29086 | 2024-11-22 04:36:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cec089ec-ca94-371a-95ea-549553b2953e | -1.49776 | -49.68242 | 2024-11-22 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebbdffe4-c451-35df-9790-b8fea4faf34a | -3.70791 | -53.753 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f15579b9-6a84-38bb-bfa2-4d777d6eebb6 | -2.69668 | -51.86731 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 60e2e241-d284-3f01-9e81-ca96dd9a33e2 | -3.63746 | -54.32053 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47df9900-fdc4-33e8-891a-f004f3141bdf | -2.40768 | -48.61246 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 914e1284-b0fd-3e01-8ce5-f082e39fb62c | -3.88967 | -43.99197 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36d8764c-2306-3060-8a1d-4b7162178c00 | -2.67715 | -46.24786 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4788f85-2425-32cd-bbf6-e610f6d01624 | -0.97202 | -52.80442 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e92e6b77-49ab-377e-8639-f304065c0837 | -3.10315 | -53.98606 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f881b9d5-7353-3d8b-a8d1-ed55d51db064 | -2.65087 | -46.24454 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19ea8542-e67a-3fbb-b619-e014177781c9 | -6.41165 | -46.9225 | 2024-11-22 04:36:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
