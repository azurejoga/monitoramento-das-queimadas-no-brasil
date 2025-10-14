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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfe840db-1154-33ab-a0ca-f5c4bc52887c | -4.65701 | -43.13368 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1f02dd4c-fe86-33a2-a687-736ee919d4a6 | -4.67009 | -43.1362 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63119e5b-cb84-3e8f-b8f3-9682e12720bf | -5.65436 | -43.60965 | 2025-10-14 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93533353-940d-386f-87ed-2a9a154c5aa0 | -4.64165 | -42.52856 | 2025-10-14 03:36:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 30c8e887-7f5f-31c0-9f0f-c12a2c1b4013 | -7.92784 | -44.12997 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a3dafe7-b647-3437-92b7-ac603a7c3215 | -9.93175 | -36.45786 | 2025-10-14 03:36:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb44f653-b40d-34d5-80bc-341de20c3804 | -4.84108 | -42.76508 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| eca88bd6-5c7c-31d2-970b-662ccc19c6e9 | -5.56504 | -41.32476 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 298f5c9b-ec2e-3016-b2d7-b19a453f6e86 | -4.66641 | -43.12381 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d5cc83da-122d-343b-b6a9-0f2d5bfda38e | -4.66955 | -43.12798 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfb03ab0-8700-3f27-93e3-04bc08f451bd | -5.87593 | -42.88126 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e55517f-ee4f-356f-8eac-aea425407c67 | -6.29877 | -42.99748 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea0b3fa3-ae64-3c77-854c-f967d46a213b | -7.90846 | -47.19873 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54f513b1-21d5-3905-9810-495a28da0e95 | -7.92993 | -44.11831 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 948116bc-40a6-351c-9510-f86dfae20411 | -4.59514 | -46.34364 | 2025-10-14 03:36:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1d76ba6c-5702-3315-8f05-f881a5a1c3e5 | -5.45813 | -37.72473 | 2025-10-14 03:36:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c0ed661-4d28-3b09-986a-229c2ce6ebd7 | -6.30255 | -46.93952 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 962bd9d9-48c9-3b34-baa8-998ce561f473 | -4.67073 | -43.13238 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c4fab14c-6a56-3bce-af79-f61446e1887d | -5.38418 | -43.22643 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a476d305-9b2e-3f61-bd0b-d53c284532af | -4.67021 | -43.12421 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6bad893e-0b3e-39f0-81b6-ce1f2c3817b7 | -7.92015 | -44.12227 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f9c220a-7e82-3c17-92d3-4165592a34dc | -10.16362 | -36.39491 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 371f2292-4fbf-30ad-9097-7d11f6d05d40 | -6.58309 | -43.92145 | 2025-10-14 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd355a32-d7ff-3f82-931a-62b8e666af3f | -7.93003 | -44.13202 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45e167d7-caae-3eb6-bf22-a6dd657afc90 | -9.93519 | -36.45837 | 2025-10-14 03:36:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3770f7b9-07d5-3aca-9df4-727ea8dc8d5a | -6.2934 | -42.9963 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e4a042a-67b9-34d2-9992-a32a3a2f2509 | -5.49645 | -43.07497 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90344188-5ac6-377c-a121-3d22b3d21f89 | -7.69355 | -42.37027 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab265a32-9fe4-3080-8d70-1586d450d114 | -7.93221 | -44.12037 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 945d987e-9d41-3a15-baf2-71d1dcfe1733 | -6.44775 | -41.82804 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b90009e-6f41-39c3-9961-daeced5e7726 | -6.16141 | -43.75747 | 2025-10-14 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d5b35a21-2f73-3e49-a891-47868fedecb5 | -7.94281 | -44.12625 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0cb69ff0-54cd-3991-b5f3-3f8bfb38ba7a | -4.83807 | -42.77572 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 15918854-e183-3dc4-ad37-0b45b6dd5591 | -7.92582 | -44.12326 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c03854fe-5d96-367f-89a6-2301b8d39161 | -7.49519 | -42.14843 | 2025-10-14 03:36:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f91c720b-218a-381e-a52d-56238dfe7a50 | -7.20792 | -45.4827 | 2025-10-14 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30f4ffc8-f7de-30c2-90e0-252bcea1e400 | -4.64223 | -42.5251 | 2025-10-14 03:36:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2d4b2bb-3f1d-3a77-b80e-21c8a5359961 | -7.81042 | -42.44128 | 2025-10-14 03:36:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a5657fb4-325a-33a6-b91c-fa472f547849 | -7.91721 | -44.12407 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20c89a7e-38c9-3cbd-afce-ff94ce29ce50 | -4.66017 | -43.12663 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2fa7d746-b727-3b97-8281-d9688f82b3f9 | -5.30918 | -45.52601 | 2025-10-14 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49055254-d52c-3124-ad1d-281c502ed27a | -6.29492 | -43.00015 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 211b5a00-e0e7-3eb1-a2f4-5523c419207d | -6.75748 | -42.8045 | 2025-10-14 03:36:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8eb823ea-4a98-304b-8780-c4e6a314a224 | -10.16546 | -36.38368 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e3414131-794e-34d6-b206-f337223a4c46 | -4.66889 | -43.13177 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f82ebdc-fc6e-30d4-9f0a-808366988ab5 | -7.21247 | -35.77855 | 2025-10-14 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf5bda97-b720-30ef-970a-a3c0ec665946 | -7.90731 | -47.20464 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 08803288-a974-34c0-a160-62797fddb722 | -6.41652 | -41.73743 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9fa4337c-6c75-3db7-bcd3-e4c56fbd0ee6 | -6.32209 | -43.90133 | 2025-10-14 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d1d9140c-388c-38bf-95e6-921f1dafeff6 | -7.75366 | -44.72454 | 2025-10-14 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a4722cf-4727-3f20-83d8-15b121ffab04 | -9.33125 | -40.87796 | 2025-10-14 03:36:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3b08ca0f-6a3a-3991-bd9c-b62c9e8a47ad | -6.99145 | -42.79754 | 2025-10-14 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| aa3da8d1-b35f-380c-a654-509ccbe5e1a1 | -8.39634 | -45.0601 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1917a4ec-3932-3bda-b562-e76b398117eb | -7.20684 | -39.45399 | 2025-10-14 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0100302d-37ee-3d6b-b014-529de842ed08 | -10.23731 | -39.95205 | 2025-10-14 03:36:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4aa29a77-5e9e-3ece-8e8b-405a730a97a1 | -5.88672 | -42.91578 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb6b3c8c-9b19-339f-beb2-1a09ba6d5762 | -5.11854 | -45.50146 | 2025-10-14 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3352e6e0-4fc5-3ff7-8682-4b80fa5149d1 | -7.64866 | -42.56638 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3561ad8a-fcc6-349c-a18c-eb795c5aa628 | -7.84232 | -41.76555 | 2025-10-14 03:36:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4b238f44-b1ff-3887-bacc-5e0414b8274d | -6.96691 | -41.68208 | 2025-10-14 03:36:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9508cc93-dbf9-303f-b321-ae0a7fc51abc | -5.89746 | -42.83619 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a201b59c-cfdf-3ba6-8ee0-d15c85cd796f | -6.22523 | -41.55868 | 2025-10-14 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 25b8d6b8-5aa4-368f-8465-aadd7b54fb87 | -7.92363 | -44.13493 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c02e35e-ca51-3e00-a266-b46b95d4359b | -6.44724 | -41.83097 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9bd652b5-1afa-38ee-8732-f3fe70d372ea | -7.16353 | -42.18808 | 2025-10-14 03:36:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84199e2b-b5d7-3d4f-ad1c-b079cef856b1 | -5.90218 | -42.84083 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68b3e1a2-073c-3729-86e7-39ba841bdeae | -7.94195 | -44.11648 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 075aa259-302a-3f19-b583-a5e8eebb2bb9 | -7.94425 | -44.11852 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9334666b-160d-364e-a4a9-87bc33e228e9 | -4.83439 | -42.77115 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9adc8834-1d0e-3356-9e02-20b412907027 | -4.85393 | -43.20683 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a518f23-d9c8-36d5-b3f1-d59f8076a2e1 | -7.92147 | -44.13287 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa3d5456-10c9-3689-8113-406acd035f56 | -5.49772 | -43.06763 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 928d52b8-08ac-3bad-a8aa-3f70a22a9c6d | -10.17229 | -36.3848 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 096480e5-bd66-3054-9e9c-dd79209ad36d | -9.99317 | -36.38299 | 2025-10-14 03:36:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5aa9daa7-a470-3bca-a93e-966b6e13e4fc | -6.53583 | -43.56325 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be8b765a-7a26-329f-a2b0-3f4c1e0616bf | -5.90885 | -42.81857 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4072723d-ccda-3c7f-b295-aa78db6eab22 | -5.21618 | -41.64841 | 2025-10-14 03:36:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0b02862-cdbc-38a9-ba3d-6cfd64585cd8 | -7.92357 | -44.12119 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6652495b-b1c5-353c-81fa-7ee63d2b329e | -4.82132 | -43.20739 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52b92c88-fe72-396a-a858-a0e4eac4dc07 | -5.99953 | -42.86961 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7b406cb4-20d1-3b01-8b50-71b4e486c55f | -7.50044 | -43.0643 | 2025-10-14 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d329b6de-704e-38e1-95c7-f6ca9668ad30 | -10.17045 | -36.39601 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| a776ba67-56c8-38bb-b569-bf8028e52d8c | -4.66262 | -43.13462 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b8275dc5-70e3-3095-8546-af1f7a877df5 | -9.16244 | -41.06049 | 2025-10-14 03:36:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b4fc1ac0-2a48-3950-a6ea-0a3a40943e9e | -7.90972 | -45.01122 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09c978f4-21ad-31c7-9c96-6c1c73f3c481 | -4.68699 | -43.12718 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e799363-a589-3832-b1e4-33174b57c95c | -4.69326 | -43.1243 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e83d4c53-45eb-3ae7-a7e3-d344c311dbc0 | -6.29555 | -42.99668 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0f0d8fca-612f-35f7-b83e-c6429eac2245 | -5.4894 | -44.99621 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d96a0b81-9f01-301c-990e-5d586b78ba1c | -6.76327 | -42.80811 | 2025-10-14 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9df2c3f3-458a-3be6-acbc-8f33c0f1d219 | -7.92929 | -44.15452 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af031623-b17d-378f-ad81-4236d819151d | -7.93293 | -44.1165 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebc3f603-e6bb-3593-b863-d0b1cfe5400a | -6.41605 | -41.74023 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df487ed4-e324-3fd2-87e7-e8280494ead7 | -4.83865 | -42.77225 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 176972aa-e330-3469-9b07-752eaca75eef | -7.94917 | -44.12348 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef7da766-989e-3883-b645-7e15cc4f7fab | -7.75799 | -44.73407 | 2025-10-14 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bc758e8c-6185-3db8-9682-e0a5e94f714a | -7.94622 | -44.12527 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96d81458-88c2-37f2-a428-fe830541c84f | -5.94586 | -43.73566 | 2025-10-14 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dac44ef5-8e4c-3eb8-8781-820fe4cfd0a8 | -10.17386 | -36.3966 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 7affb337-f6b1-3c0e-bbd4-a2204463f365 | -6.30945 | -46.94073 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
