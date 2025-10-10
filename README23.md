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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f9b1de0-f43a-3bdc-8c54-057cd034b7ab | -8.51257 | -46.14789 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a39762-4f40-3daa-909f-f0cc1b5f466c | -7.25602 | -42.96498 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 325befae-41c7-363c-96bc-66a524c8eb6b | -6.98303 | -42.03513 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5e6cb11f-6172-35d9-9c2d-082488eabefc | -5.08817 | -42.48792 | 2025-10-10 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebf1a360-74eb-36c4-b100-fc6782a230dd | -6.82428 | -42.7895 | 2025-10-10 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4a9980a0-6e44-32d4-99cb-b5fb0302eb1f | -4.89176 | -41.54121 | 2025-10-10 04:00:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 259ed4c1-1618-3e72-88e0-3fda47be14ed | -5.42171 | -41.36399 | 2025-10-10 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75fae304-a8c4-34e2-8c67-449968666be2 | -7.52108 | -42.00453 | 2025-10-10 04:00:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30684690-bbd8-3022-b3fd-2f2fc32d3c99 | -7.41034 | -45.92209 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b0619a5-9883-3489-86b6-41a540d0ffbb | -9.65999 | -43.84632 | 2025-10-10 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| db378344-1100-3d0a-8823-cfd3e6301dde | -5.90604 | -42.85282 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ecce98f4-9548-34b3-9897-c5300fce9134 | -6.95762 | -39.48446 | 2025-10-10 04:00:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45094694-3957-3b29-8d3b-4aceff57874c | -7.71374 | -42.37722 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e57eedb-1159-3414-acf3-3ee016a40f69 | -4.94862 | -42.82207 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bedc2126-6068-3e2c-8830-ceb06bb3c019 | -4.24331 | -48.20699 | 2025-10-10 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f58dae8-7ffc-37d9-9230-2395f5a0e251 | -8.84076 | -46.05921 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dbd230a-cb79-3dab-b9bc-7f9fad11ef9e | -7.797 | -42.40191 | 2025-10-10 04:00:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b988621-3f63-342e-8643-363f976508d4 | -7.69105 | -42.38531 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6f39113f-a0dc-334a-950c-50b15374e193 | -5.74925 | -42.76059 | 2025-10-10 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a223f888-2771-364e-84db-35eb179cc5ea | -7.2449 | -49.51991 | 2025-10-10 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31bdfb9b-6de7-37f4-bef0-46153a195489 | -5.99434 | -42.47946 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c27be970-c284-31d2-bfc7-19e837f3a359 | -10.16345 | -44.60442 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55d90961-dba5-3e27-967c-8c90fbebc19b | -4.24385 | -48.20374 | 2025-10-10 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77b00601-eca4-3a14-8228-1aa3a79ef4ec | -6.58877 | -44.6232 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 37d96604-ae83-3fd5-a984-d04276567730 | -5.40849 | -40.98452 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b9a6e618-78e4-3432-9e07-4f8ad5d351e5 | -7.80129 | -41.65895 | 2025-10-10 04:00:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50541cac-b209-3a4c-ae48-3a3385098044 | -8.52679 | -46.16681 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d75d166-6022-3873-9960-d570a217700f | -5.84986 | -42.29868 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ae98874-5804-3f9d-9a6f-02e450e91062 | -7.79791 | -41.6584 | 2025-10-10 04:00:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffda6efd-db89-341a-9904-bfddeae3993d | -7.79619 | -46.02308 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 517f5e6a-d1f9-3ed2-a672-fb1c5559c52b | -4.65059 | -43.19468 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f9c2506-8360-3cba-968b-5d5c1d439d73 | -8.00991 | -43.75982 | 2025-10-10 04:00:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07c9a1b5-3996-3bcb-b5c8-4cc613a1cbce | -6.7496 | -42.82869 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8992380b-d0c0-3f16-aad6-7cf6e704df95 | -6.53531 | -44.36093 | 2025-10-10 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31915182-e893-373c-adae-d0610ba808b0 | -7.83907 | -44.55098 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 343894e4-63f1-32e9-ae7a-0cc8ff878f1e | -4.84398 | -42.93447 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2c65c4f7-35b4-3921-880e-44184b8ea208 | -7.08328 | -43.51773 | 2025-10-10 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3766f9b5-56be-36e7-addf-f29926f0b5e5 | -7.80281 | -44.12132 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a2f3a4-9a4f-3df9-a5dc-065b311c8b86 | -7.11981 | -43.27041 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6da02ddf-e7d0-3e6e-80e1-0710dd5ccbd8 | -5.97886 | -45.92139 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea2ded1d-fdab-39af-bad1-b15e8c98bd3e | -7.27704 | -41.97297 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4541b686-c7a0-31b5-b177-0e2d06ea8009 | -7.4025 | -45.91657 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 858f1480-f6da-3aad-ad3d-d0487371a7bc | -8.68707 | -46.72322 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b78d5d9-8bb0-3bf8-903c-4fde663e60f9 | -6.5783 | -44.628 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9cef6c7-5361-3ab9-89d7-fa27c5b37524 | -4.1439 | -47.6552 | 2025-10-10 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b8a68a5-5bfd-3b37-b782-0bfb0e8c1296 | -6.75342 | -42.85045 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e62eece-0f2a-37bc-bbbb-de82441c8568 | -8.90096 | -46.01278 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e16861c1-b09e-3768-9e38-37bf268db47d | -5.68917 | -41.72704 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 478d55a0-9a83-3684-a121-1a452fb83692 | -7.62405 | -46.65457 | 2025-10-10 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64b4be8a-39cd-3634-b4f9-c3711c3b2145 | -4.55494 | -46.68577 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3e05d203-2feb-39bd-baf0-746f7af606b9 | -7.77624 | -44.04688 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d9501ea9-b3fc-360e-a303-8d4e52075323 | -7.41727 | -42.97172 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| afec2d2b-1427-34f5-a6af-1ccc9eb6516e | -7.09645 | -43.25328 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7e5088c5-f131-3b3d-a8ae-0389263ac5b7 | -7.20507 | -45.49162 | 2025-10-10 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cfa9268-8530-3b83-b953-5be9d6469b9b | -8.20894 | -43.35286 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ff9ec7f5-1df5-3394-aea5-190193817e07 | -4.39646 | -44.08886 | 2025-10-10 04:00:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fcf4e38-e996-3ef6-a9e9-8b40d17af51f | -6.98572 | -41.931 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d530ec7-b36d-33fd-82f2-a99e8d94764d | -4.72146 | -43.35088 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ea149e1c-4a08-3490-be0e-2f7a2dbd4601 | -7.99025 | -44.46372 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f563417f-40f2-3574-9006-ec320fe13c25 | -8.84042 | -46.06222 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f9e49dd-91fe-3797-9b44-638eaf20a234 | -4.54936 | -46.69011 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0a7336-b494-3811-9b40-dc30d8a24fc9 | -7.14716 | -42.18909 | 2025-10-10 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47ae5b18-eab3-3938-a58c-d9fee20ae825 | -5.87993 | -39.10163 | 2025-10-10 04:00:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7231770a-4ec7-3f4d-b807-45cef4190969 | -5.41951 | -41.72858 | 2025-10-10 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5243e14-1587-3069-abb3-7c3c59d29dd2 | -10.15904 | -44.58457 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a0b4c1b2-7d01-31d3-8185-d0f4e13ee3de | -7.28451 | -41.97033 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d72cb7c-0994-3d4f-8238-9848573ef77e | -5.33016 | -44.82133 | 2025-10-10 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d9830ff-4963-374e-955d-4db17ac1f7ae | -5.95553 | -45.67974 | 2025-10-10 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3dcc8317-1290-3f0d-ba54-eb2bd6594336 | -7.79673 | -42.60901 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b9784955-06f8-37d1-99e0-ae2e42d2299f | -9.5417 | -43.25798 | 2025-10-10 04:00:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 192a1755-af4b-3da7-b410-ca2177d5c211 | -5.61723 | -41.16941 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43f3e968-005b-346f-b752-a0b7e6704c0a | -5.58364 | -41.22762 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94935498-4940-3378-b73b-14706ca78a1b | -7.49779 | -43.11956 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43941c4e-5db3-3173-aed3-773dc7b88a75 | -7.90102 | -37.06025 | 2025-10-10 04:00:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7ce35c3-44ad-3e85-997a-a91b7fcdf5f6 | -5.05571 | -45.85423 | 2025-10-10 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a7656d-ca7b-3e32-9bf4-c56122f70a2c | -6.59192 | -44.62891 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09f2a3cd-1c6e-3f6f-aaf1-9e80738c75d6 | -7.67481 | -42.57413 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 924af85f-e280-33d1-bb52-895c1a7a59b6 | -7.33498 | -47.81965 | 2025-10-10 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8caa21ed-4d1b-3140-beaf-52ed9cba0e1d | -8.16416 | -43.3253 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| df518b5f-8798-3a9d-9dd3-fdcc5d4a6885 | -9.08014 | -45.04053 | 2025-10-10 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0268367f-1d52-3adc-a256-64841a19ac8b | -8.20691 | -43.35832 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa49be1d-0f4b-3ed8-9b21-52bab859f870 | -7.40538 | -45.92542 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8088f29a-9bca-331f-b6bd-074e92eeeaf4 | -8.51472 | -46.16059 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ad57232-ba8e-3958-872d-3fc53e1dbe54 | -8.19814 | -43.34396 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 31f0a566-867d-3973-b9cc-3439b9f9e0b0 | -7.13222 | -44.13829 | 2025-10-10 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3327ff0-8dd9-3c52-8520-9e94b7f0a5ff | -7.61194 | -43.06493 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7b4ecfda-6f53-3280-b2b6-93e97506bb87 | -5.78243 | -42.57983 | 2025-10-10 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b7fd3bb-2df9-308f-b8ae-fb63a9cf4261 | -7.79284 | -42.60482 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b7d8569-98eb-3ac7-abde-c4076231245f | -7.42663 | -42.98167 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ab796670-23e9-3927-ba62-f0ce9e1cf5ca | -5.90292 | -42.85511 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 81dc21cc-5294-3cea-9810-7aa131bd0e8b | -6.70291 | -41.55453 | 2025-10-10 04:00:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d522c1fc-eacd-3a2c-ae41-89978919f299 | -8.20984 | -43.36308 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6fe0c5e1-223a-327a-82dd-745a08214b89 | -7.80582 | -44.12656 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa7eb1a-f09b-3b3a-b322-dc7990dbda46 | -7.40608 | -45.92132 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90db03f8-5142-39e9-b875-41eaa4a0f567 | -5.42112 | -41.36767 | 2025-10-10 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8b0b6f48-a489-39e5-8edc-046b04928c39 | -10.19273 | -44.59323 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 30de045c-73d8-3799-b8d2-200c9b31a2e1 | -8.20402 | -43.38203 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 20310898-e9cc-3f0c-b555-5c7728c369d1 | -7.09715 | -43.24903 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0239ab77-7614-3fd6-a19e-7c0b8fa8c725 | -7.77908 | -44.05492 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4e507f7-fa50-3c45-8032-de4c6fbb4341 | -7.78571 | -46.55079 | 2025-10-10 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)
