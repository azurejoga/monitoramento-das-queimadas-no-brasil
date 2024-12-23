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
| 0c870d40-6822-304a-b37c-ef498ebcccf2 | -2.40482 | -53.73909 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7ea6ee1-4de6-3948-958a-dbfa296ea800 | -2.96678 | -54.2256 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 631522a3-e7f3-3346-9496-bf4d4ad040a4 | -3.09845 | -54.55201 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4052cba-bc8d-3222-a1bc-73e04edabc89 | -1.94122 | -48.94457 | 2024-12-23 04:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43dfe4c5-7e97-3c63-b667-26197386c4b7 | -1.06527 | -53.61722 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9498192-2d51-320a-a579-1d908ed011ec | -1.26011 | -54.14585 | 2024-12-23 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d7edc48-c0a4-39ec-a500-87e5230d93b0 | -3.77705 | -46.82272 | 2024-12-23 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91af623f-7ce5-349d-989f-dc3053108fdd | -3.87329 | -47.28265 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b5e0fc5-622f-3b19-8d55-1de6bd265eed | -3.99229 | -46.96028 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d35554-9e95-3838-8ef4-531abdde8997 | -2.06617 | -53.45231 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d69239c2-0a21-3f0f-8f39-d40a4899d29d | -0.6257 | -49.62033 | 2024-12-23 04:53:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72f246f6-fffe-3581-8a0c-a2a0e6fd87d0 | -4.09377 | -45.30857 | 2024-12-23 04:53:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab8ecb58-bf71-3110-b21b-efe86e97018b | -4.15317 | -43.65917 | 2024-12-23 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2fdebe5-02fe-3018-aaba-d7697b39ac4b | -3.90124 | -47.0032 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4243c60-1515-3652-8094-1f0acbf4a49e | -3.18584 | -50.55245 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd728f0e-5ea3-3307-8534-e0b66f8f0103 | -1.06581 | -53.61376 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97f4b6f9-b60a-36b5-9aa0-1ae64dcf14ec | -2.12783 | -50.70438 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0467d946-fd98-3c1d-a9a1-134faaf846b5 | -1.4947 | -55.09683 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b57d0623-7a38-3bd6-ac06-b915fe17e2eb | -2.97446 | -53.87428 | 2024-12-23 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54dcbef9-f168-39c2-ac90-590bb793e270 | -1.36195 | -53.6963 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108e86da-4daf-3eb0-b076-fc7f6e2ea2b4 | -2.04298 | -52.10775 | 2024-12-23 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3df70032-22bb-377f-808a-fbd79bdf3b8c | -3.09901 | -54.54847 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83d5ff96-53e7-3eac-ba36-83ff63dd635a | -1.31416 | -54.08596 | 2024-12-23 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3100dcd1-b91c-390c-8f0e-e78c2ff6562a | -4.37217 | -44.00228 | 2024-12-23 04:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30f94965-eb94-33e6-843b-639777fd9028 | -3.00254 | -48.12571 | 2024-12-23 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 899588c1-9917-39ad-aac2-9eedffb0e1f4 | -3.33001 | -53.10423 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 652eaf9f-64ef-3793-b83e-ac9426dcc3d1 | -2.93373 | -52.81616 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5d6cf24-7b5a-31d4-a8fb-acbbba000e3e | -2.80236 | -54.03911 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 445645c0-c38b-3318-8855-d032076c3c4f | -2.80036 | -53.06021 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fad4f841-8dda-363f-8792-fc92c47c2c8a | -3.87768 | -47.28329 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f3b6ae0-d01b-34e9-a475-35b73883505f | -3.00774 | -48.11906 | 2024-12-23 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21437d81-d7a2-3a23-8ebf-2a69e647f5ea | -3.43198 | -51.10879 | 2024-12-23 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adacc11e-6aaa-384a-9062-50424cdb4f14 | -2.40704 | -53.74652 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eceae543-c8e0-3cd0-9225-438392f40fe6 | -3.18647 | -50.54844 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 708dbba3-3f70-31ea-ac59-f598e2cac5a7 | -3.06809 | -52.84793 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49c6506b-ff74-3c12-b29e-bc755cbcc94e | -4.04132 | -46.4094 | 2024-12-23 04:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8639bc6e-77fd-393a-8d14-2cf3bc6c3385 | -2.56385 | -45.5016 | 2024-12-23 04:53:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ff364b-e632-380c-b8df-46262cd9353f | 0.65116 | -59.7394 | 2024-12-23 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6a021d9-c11d-3e18-bd81-c2cc9bef15bb | -3.63203 | -51.30921 | 2024-12-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 453e2705-f32b-31b1-9c36-de3afce232f7 | -6.95179 | -43.53899 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ad1803d-7188-3123-8150-df5407bc4573 | -3.65255 | -54.73684 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc2ed9b9-a9e1-3d69-bc13-2e6f85a07175 | -5.45428 | -44.81019 | 2024-12-23 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2301cb0d-8a86-3d2f-be53-d51e7abef6d6 | -5.93117 | -45.49028 | 2024-12-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 945eaa48-6d3f-3207-86c4-9c82b2d82d49 | -5.44797 | -44.81627 | 2024-12-23 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dee1f56-9db7-3746-a649-68edcceee85c | -6.93997 | -43.53725 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 34e74d73-3958-395e-8084-d474bee7fc6c | -3.15038 | -54.56407 | 2024-12-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbbdbd85-c89c-3617-9b93-380c814b3f28 | -4.52902 | -46.36081 | 2024-12-23 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b265a2a-122a-3066-9343-4ba070d8eef3 | -6.00402 | -45.42005 | 2024-12-23 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 738b8684-2e05-3e9b-bbd8-ce519e0cbfb1 | -4.71976 | -46.46275 | 2024-12-23 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d73ebcd-af9f-36d8-8610-615c6926b3c3 | -4.48658 | -49.06591 | 2024-12-23 04:55:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f171fbc7-cc39-3442-b8aa-b5a7a224d85a | -6.93277 | -43.53114 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 90eca57c-8987-35ae-ad13-d1d9f747d8d6 | -6.94116 | -43.52874 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09a2a6df-eac8-3960-b875-7916cfe19c9b | -4.03287 | -50.05815 | 2024-12-23 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ed3adfb-40a1-36c5-829d-281f92742d83 | -5.4538 | -44.81355 | 2024-12-23 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 685eddcb-30af-322f-9aaa-a0e51314207d | -3.75604 | -52.3794 | 2024-12-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2eb9e93a-a570-3616-9d16-c1fa14e92b38 | -6.94589 | -43.53805 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2990d546-57a1-3ace-a88e-3310107af8d6 | -6.22646 | -55.65666 | 2024-12-23 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88afcf63-682d-3ed4-9122-509198327eaa | -5.44894 | -44.80954 | 2024-12-23 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29dec401-dce5-32cf-bbca-1358c71df52d | -6.90915 | -43.54206 | 2024-12-23 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62ad0c82-2ebe-3391-b7d7-1fa000fa4284 | -3.14703 | -54.56355 | 2024-12-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3a008f1-76f9-30e3-95b4-464224ec7f7f | -3.2643 | -54.10444 | 2024-12-23 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37365c39-6e6a-3917-b724-ab4d3ea4c070 | -3.63772 | -54.7529 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35af8f3d-e4e5-34f1-bf29-5cf3a1c58ffb | -4.06028 | -54.74278 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 390d0b40-2660-346b-aaf2-cfc5f0919ad6 | -6.93404 | -43.53654 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 49ea0266-e49a-35ed-bde7-20abb37b102b | -6.94648 | -43.53385 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 00f63a69-23cc-392c-8cc3-a693352554ae | -6.22307 | -55.65612 | 2024-12-23 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09212345-8fad-38fe-bd39-0f64be8425cd | -4.4458 | -45.93134 | 2024-12-23 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9a4d08e-b121-3229-929c-93458be5515f | -3.34359 | -53.32183 | 2024-12-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4581e94d-4610-36f3-bad0-d9ec7afbd174 | -6.9387 | -43.53189 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b6309543-52ac-36d9-b40a-a94ba0e26cc8 | -3.68834 | -52.48426 | 2024-12-23 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e005bf23-0b21-31f2-9105-a733b88962d9 | -6.93936 | -43.54165 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 67864a9c-6c79-35fb-8ca0-eda4ea63fb15 | -3.76775 | -52.37029 | 2024-12-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e37b07a8-aec9-3f53-ae9c-4b2d5cb99e36 | -3.94463 | -54.63444 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2b9dc03-a1c3-32ff-98dd-03b6a20306b0 | -6.93464 | -43.5322 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5df6e227-35c2-35b7-9f03-b2bd53807394 | -6.93814 | -43.53619 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| df053764-8ef2-3c63-b74c-80831a0fc665 | -6.90266 | -43.54546 | 2024-12-23 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ac3227e-31cf-386f-9557-ede4097415de | -6.94462 | -43.53279 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d0a81a9e-7bb0-37e8-a4f3-3c0722c47740 | -3.14368 | -54.56302 | 2024-12-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f10eabf4-e36b-30d7-9458-2ae5cb81cc68 | -3.14033 | -54.56249 | 2024-12-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26051f72-8f5c-381a-b750-427be090bd4d | -4.49051 | -49.06648 | 2024-12-23 04:55:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48fcd4dc-0fa7-35a8-a894-1d8e0b10a486 | -6.9322 | -43.53549 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0e483a84-4e46-3bf7-b17c-0c3bcc34afd4 | -6.21693 | -55.64392 | 2024-12-23 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a30c482-12c9-36ec-9c54-8f056c788e06 | -3.53204 | -53.2666 | 2024-12-23 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 039499fc-74a2-35fc-8018-ce3a27b563ec | -5.44845 | -44.81291 | 2024-12-23 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e40f431c-7dc3-3037-a7a4-591598012e26 | -5.05854 | -44.23745 | 2024-12-23 04:55:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bc74699-4900-3238-8308-eb0e824f181d | -6.94997 | -43.53793 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff19df5a-1b86-3cd0-a243-2f1a06dd14e2 | -3.68654 | -54.33478 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 645623bd-8de1-374b-8f95-050f68d2d7d2 | -3.685 | -52.48375 | 2024-12-23 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec07c1e9-a546-3132-bf23-fafa4ab3c9d1 | -5.43741 | -47.61428 | 2024-12-23 04:55:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4ea8a2e-f03f-3722-8417-bab5c81a8462 | -6.94057 | -43.53299 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 26df3976-0e7f-36fd-9633-8f645b491b8a | -3.86677 | -51.21962 | 2024-12-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5592b61c-7e13-314d-8ba5-3855b765fb0f | -6.94349 | -43.54132 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 49a75893-77fa-3d37-a08d-e900c8d97a75 | -4.03219 | -50.0625 | 2024-12-23 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7eb6d58-0d07-3123-a9b4-bc4dd30d6fd9 | -3.65003 | -54.74025 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf33bb4f-df10-3711-bece-934b913bb7e8 | -6.2175 | -55.64032 | 2024-12-23 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 601065dd-4a8a-3734-b5e9-c39068b28fff | -3.94798 | -54.63496 | 2024-12-23 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 970d2c1e-ad8a-3544-99cd-3648837fb806 | -6.90325 | -43.54118 | 2024-12-23 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bba5d8c-fc76-3256-bd6c-b4559fb62424 | -4.12581 | -54.94968 | 2024-12-23 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9c27167-fe3c-3591-8ce4-137812890f09 | -3.14311 | -54.56655 | 2024-12-23 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e57cf3d-ce18-3306-bc11-403919ecde8d | -6.93524 | -43.52787 | 2024-12-23 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README18.md)
