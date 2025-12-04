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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61e0c2bc-35d4-31d4-a9c8-dc075312ee5c | -3.38437 | -47.27991 | 2025-12-04 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a4fe54-3492-33e6-9280-41d38e17c425 | -3.06523 | -48.03938 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ab0c8d3-73b7-3b67-9f5f-8a506d876510 | -4.49841 | -45.76867 | 2025-12-04 05:10:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9e9f256-060d-3285-9db9-20eb092877cd | -2.42056 | -45.79634 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a75bfa8-0c6a-33f3-b448-c9d8dd5f99cf | -2.92081 | -48.23405 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f04febe5-db22-3111-8bb1-6bc0f16afd85 | -1.25481 | -52.86852 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98bbc567-19b9-3b45-954d-2dbecc0fafa5 | -2.60544 | -49.25639 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3610eb8-aaf8-3c49-893a-63879873c3a3 | -2.41932 | -48.59205 | 2025-12-04 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9fd9bd-1245-3ca2-88ec-bf7b63a1d42f | -1.53965 | -54.19413 | 2025-12-04 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4453c975-25bc-34a2-aae4-20e2bac4ce29 | -4.03313 | -46.973 | 2025-12-04 05:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33c528fa-91a7-3260-86df-f604e0cd0db9 | -1.98365 | -47.96743 | 2025-12-04 05:10:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c3139ff-356b-3da2-acd1-2ea66a112288 | -1.09316 | -54.11241 | 2025-12-04 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e345505b-e471-3775-b7a7-6e27ef6bc795 | -4.55576 | -45.804 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d9377fca-f2f5-3a27-b964-2c41e7b51ed8 | -4.06313 | -46.56883 | 2025-12-04 05:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 40c6546a-c75e-3689-b04e-d87948b3f7a5 | -1.35558 | -53.2267 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5507120-a6e4-3438-8784-8f9023e38fb2 | -6.43008 | -44.78915 | 2025-12-04 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 202c2f9b-f682-3475-856a-e08855333543 | -4.50385 | -45.77443 | 2025-12-04 05:10:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4379f9de-8a21-380e-a754-45313a6e8354 | -0.83868 | -52.35071 | 2025-12-04 05:10:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a6839b7-b7be-3273-9a90-2ba9c38de6d1 | -2.4838 | -47.83303 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af62c829-8c3a-3822-b2a2-53ed1fe1e363 | -2.92127 | -48.23107 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c03c3e-41c5-3259-bfbb-28d60b43bb7f | -1.42683 | -53.01442 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbfef838-ebd0-37cc-865d-00a28c0ea7f9 | -0.4145 | -51.62919 | 2025-12-04 05:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0bf0422-144d-3092-aca8-a1677606d233 | -3.04956 | -48.42524 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0cda9c1-0b9d-3ecf-aeaf-30dc5d395795 | -2.63432 | -47.31159 | 2025-12-04 05:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffc983c1-f44c-3e38-a2ee-02903730bb39 | -2.78571 | -47.4359 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3b643b3-c8a6-32a3-abee-9daf9df8709e | -4.33409 | -48.76859 | 2025-12-04 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56942646-3087-3f9e-bdbc-ec56275b5b93 | -2.60072 | -49.25565 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47c07486-0ef5-3384-863d-5dd1fc47e4de | -3.22033 | -48.61748 | 2025-12-04 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e2994af-0a94-3f33-9b0d-405750ee9d5b | -2.61017 | -49.2571 | 2025-12-04 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a09de799-8a77-3e51-99ac-f6e9d367044a | -4.7721 | -46.13064 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78920628-abcb-30d7-85a9-828f339d1449 | -3.0657 | -48.03622 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17d69585-5c00-3dad-9e76-0b413a4a0742 | -2.91895 | -48.23156 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7a149b4-2ff6-33dc-93f6-c24bf7bf2efe | -2.69155 | -48.45568 | 2025-12-04 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb2f4ee7-c22b-3c30-a0e0-d4f064bb7806 | -1.87705 | -50.96083 | 2025-12-04 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a70d01e1-78ee-386b-b10a-008a8308f761 | -4.4705 | -44.25903 | 2025-12-04 05:10:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcd74550-9e67-34d2-a016-8f61a3a44f9e | -1.09375 | -54.10867 | 2025-12-04 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77e68020-cb6f-3185-9b1b-935c374c2e34 | -3.39037 | -47.27727 | 2025-12-04 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 958b2a2f-b6c9-397c-8da8-9fb9a99eb7b1 | -4.47307 | -44.26176 | 2025-12-04 05:10:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80582fb5-59b7-3775-9185-c209366ef570 | -3.22489 | -48.62109 | 2025-12-04 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afcdf4bf-cf73-331f-8c09-39b47cd961c3 | -3.39136 | -47.27616 | 2025-12-04 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61be741d-0ef1-3142-ac12-f25be2595330 | -5.98275 | -44.59547 | 2025-12-04 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63e951aa-4057-3945-b670-c6a1d0dac7b6 | -2.63091 | -47.31105 | 2025-12-04 05:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9201b92-b38f-394a-b9e5-e9e4f02bf092 | -1.1615 | -48.86473 | 2025-12-04 05:10:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c5181de-a048-30be-97bf-d57eb9b43f84 | -1.12607 | -54.19407 | 2025-12-04 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 615c9aca-efd7-39c0-9d58-ad01a21a9d6c | -2.63641 | -48.03589 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 271e5e37-afae-3c38-a856-2028845224f3 | -5.97517 | -44.60061 | 2025-12-04 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df199a70-f2d3-3ea7-b9fe-6a4e49c8b7c5 | -4.55558 | -45.80658 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e9bfd4a-944f-3108-9040-97398f11287a | -4.60254 | -46.00008 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6573bbc3-72be-31ef-957f-e1cb8aecb340 | -1.12186 | -53.44653 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3b625e-37ad-3456-916e-1d5a1ae618e9 | -3.04452 | -48.42447 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ce67fc1-116b-3ff1-85b6-7b71c68cb6c1 | -1.42747 | -53.01021 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fa683ee1-b328-3d15-9608-65a4eda46553 | -1.12249 | -53.44255 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00467d65-9d44-36bd-bacd-ab510762350e | -3.03991 | -48.42078 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6e47832-266d-382d-82c9-d189a6300d20 | -6.42175 | -44.80046 | 2025-12-04 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be8bb88e-d82d-3488-b7b1-0e7a5ba67d7b | -3.0454 | -48.4186 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad4ff00-6dcc-384b-a67a-c4addea08826 | -4.67527 | -46.38506 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66b0fe19-5ecd-3738-870a-126fe491f9c2 | -6.43682 | -44.78971 | 2025-12-04 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 906289f1-a150-3574-900b-963c789d4f7a | -4.69241 | -46.43499 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d228cf1-2a45-3b78-8717-7b07242856e9 | -2.1374 | -47.88697 | 2025-12-04 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9cc11bdb-ac76-3d6e-acb1-24fe907802fc | -2.87546 | -46.80651 | 2025-12-04 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49d9e8ed-c432-3c47-84d9-b1c2f0d0603a | -5.97849 | -44.59536 | 2025-12-04 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebff6b5f-7964-3661-a33b-1db04d073c96 | -3.05416 | -48.42889 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38cb780f-e305-300e-8f53-f461aa7d771d | -2.07447 | -48.3708 | 2025-12-04 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9334d738-7bce-3c23-a8e4-30ef9bdc2765 | -2.5387 | -45.37561 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c130dd2-28f1-39eb-ae05-d49263bf4f3c | -6.43603 | -44.79562 | 2025-12-04 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4e53808-94c3-35e1-bbf9-de6f81c62df2 | -2.52644 | -49.46167 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18818928-d07a-386c-b3ba-3f063a3d0b20 | -2.5394 | -45.37093 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 020cfb5d-6651-3a12-ba4d-284fd2445dc8 | -2.62838 | -47.31425 | 2025-12-04 05:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 529c328a-83c6-3500-8061-a427da451485 | -7.21391 | -45.04948 | 2025-12-04 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d61100c-558f-3307-b33a-e3c499880830 | -6.42929 | -44.79503 | 2025-12-04 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8954188-2a00-3fe2-acda-05f6a9803a97 | -2.42253 | -45.80319 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02498a8e-f556-36ee-b585-78ea2cd5e69f | -4.69474 | -46.43285 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ecb97b0-73e5-37fc-848d-f271a43a4e1b | -5.98192 | -44.60145 | 2025-12-04 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 255cd48e-75b6-3fd9-b6b2-88448b8f5a81 | -2.06481 | -45.35564 | 2025-12-04 05:10:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4af7365-b686-3e9d-80eb-99e8ea87630d | -3.04496 | -48.42152 | 2025-12-04 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f49acb8b-7948-32e6-9f32-20f301ba59d9 | -4.47392 | -44.25568 | 2025-12-04 05:10:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6ebf35c-c854-364e-a5d1-1adf4d824c23 | -3.38587 | -47.27539 | 2025-12-04 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19efeb75-47e5-3c44-964a-b87ef9819b86 | -2.79174 | -48.90469 | 2025-12-04 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4273935a-ff02-3543-9c6b-32e05d826edc | -4.60321 | -45.99541 | 2025-12-04 05:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d560a5bc-8ef6-304b-a515-cca1f53ab5ea | -1.42319 | -53.01384 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e177fd79-d566-3154-ab51-1bf000656c3c | -4.69832 | -46.43582 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f6127d6-65a6-3b26-af8a-a7dbac757755 | -2.38346 | -49.39179 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| feb20b09-0fda-3640-be52-2c35fbbd370a | -2.48948 | -47.83065 | 2025-12-04 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e08a6dc-4cb8-3d56-a159-383361780f3c | -2.13787 | -47.8839 | 2025-12-04 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1568bf7-fbbe-34b7-8267-068b3cfaf300 | -2.41992 | -45.80074 | 2025-12-04 05:10:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 879acf6a-1dfa-30cb-a9bc-7a99529f5926 | -1.42681 | -53.01125 | 2025-12-04 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 40064ad7-3ec3-3cf6-b9d3-44b91ed62f34 | -2.42051 | -48.59355 | 2025-12-04 05:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aac230d9-e4e9-34cf-94a9-610315a729b8 | -2.5372 | -49.45341 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 21d82a88-44d0-31fb-9ef8-62db931eb227 | -4.67729 | -46.38748 | 2025-12-04 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76bdee90-4885-3731-8632-f23a0bf10c12 | -3.38536 | -47.27892 | 2025-12-04 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0638d36f-47c0-30e2-86db-21f49876af37 | -2.42885 | -50.29205 | 2025-12-04 05:10:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3b927ae-0d48-3ebc-a824-a7fa1c21dc38 | -4.05052 | -46.61496 | 2025-12-04 05:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18dbec49-044d-3dba-ba8e-0190e561f954 | -5.98445 | -44.60217 | 2025-12-04 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95e0257b-ff3a-3116-a1b9-874931ea98d2 | -2.63041 | -47.31449 | 2025-12-04 05:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de027cf7-675f-3c41-9d8e-d17e90aec54f | -4.33344 | -48.76951 | 2025-12-04 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7d3dce1-b0b5-3f25-b160-9a9a84987308 | -3.21991 | -48.62032 | 2025-12-04 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24553f6d-0cf3-3f96-8c0b-cda4a2c3e847 | -2.14302 | -47.88475 | 2025-12-04 05:10:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50978031-64d1-3e97-aeb7-b9df3ae32a79 | -5.9777 | -44.60138 | 2025-12-04 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21ae2057-a24d-3251-8905-432b98b08ac5 | -5.98525 | -44.59615 | 2025-12-04 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c78fe5bc-cab5-344a-9fd0-1f385676c313 | -2.48318 | -49.41438 | 2025-12-04 05:10:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README20.md)
