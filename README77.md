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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb9dc513-855c-3764-846c-e8ba155f812b | -20.07391 | -45.78113 | 2024-10-05 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b97ec13-341a-3a58-8bcb-f538419773cd | -20.07334 | -45.78481 | 2024-10-05 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f451dfe6-8014-3b8d-9478-4d8df3d66363 | -20.07277 | -45.7885 | 2024-10-05 04:17:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 047b806d-dd9b-350b-8fdb-8f119a29d687 | -19.79939 | -43.67812 | 2024-10-05 04:17:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef68939e-7a72-3fa9-9b58-5c612c3f10b4 | -19.76208 | -43.6385 | 2024-10-05 04:17:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5abca047-ef15-3b49-a31c-6f5f323ed8b0 | -19.76175 | -43.63997 | 2024-10-05 04:17:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd206c6e-4b70-354d-89b1-85461bf181d8 | -19.28752 | -43.78709 | 2024-10-05 04:17:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e277b4-18e7-319e-99cd-3237411ae6eb | -19.24077 | -43.36495 | 2024-10-05 04:17:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76587ecc-fc58-3a1a-a72e-b7ef5dd3b671 | -19.23726 | -43.36428 | 2024-10-05 04:17:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b65341d-4966-3148-ae8f-8150f8ae129a | -19.23666 | -43.36848 | 2024-10-05 04:17:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ce3a6a9-dff8-393f-ab11-49f6aae50087 | -19.23135 | -43.38031 | 2024-10-05 04:17:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| befbe398-f117-3ba4-936d-c8296a7058c7 | -15.70393 | -48.32356 | 2024-10-05 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9263f9f-a263-3c88-8af9-d4089d99b2c2 | -15.53384 | -50.24638 | 2024-10-05 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9992be91-93b8-3c2f-852e-73bc2e44dcfd | -15.52943 | -48.5085 | 2024-10-05 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dc6add9-07cb-32ed-8ea8-1bbc8850ada4 | -15.38001 | -48.59837 | 2024-10-05 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d790ca9c-82e6-3c82-b6c0-31074a2f6e51 | -15.18549 | -48.07577 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8c27f5e-cba2-3100-8371-22c16bc12b3b | -15.1798 | -48.06591 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6110920c-60ef-3d9c-a2df-99382f449e2b | -15.17337 | -48.06036 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23eaada5-5721-3286-b4e4-72b4d848c880 | -15.16979 | -48.05969 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473fa25b-80d1-34e4-bfc3-82843ff6b3b9 | -15.16766 | -48.0648 | 2024-10-05 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dae53320-0083-3364-9c5d-e0bc9dde2f50 | -14.8284 | -48.81151 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d6038f5-a27f-3626-81a4-d0b16a38a044 | -14.82488 | -48.80869 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24bbc12f-f6f7-3bb6-bde5-83d33dfd1861 | -14.82467 | -48.81073 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 646bd6d5-12d5-31a4-ad74-9dd44cf26b02 | -14.82407 | -48.81344 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b990a81-3c2e-3585-ab19-06b70f63da5c | -14.82381 | -48.8156 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d2250f9-aa7f-3cc8-b8cf-56d98f6fea6f | -14.82323 | -48.81844 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac9f5ef3-6b80-3e44-85ad-da86222e1adb | -14.82095 | -48.80999 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04d8ce83-f07a-3ea6-b5a3-a6706ccf3642 | -14.82034 | -48.8127 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa8dd46b-8b1c-3f9d-a6f3-9d37913a2287 | -14.8174 | -48.80738 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d9ad810b-671b-305c-a740-a4ad2c656628 | -14.81632 | -48.81428 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec8c3264-454f-3d4a-ab90-a8d86dcafa14 | -14.81257 | -48.81369 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3ce60c0-5d73-3573-b544-81febd34ef29 | -14.80821 | -48.81601 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 133db72e-0b59-3f71-adbd-30a54ce9513c | -14.80528 | -48.81063 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fdb7a379-8877-3dc5-a5d8-50634259871b | -14.80445 | -48.81548 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77858b34-2319-306f-a32f-fca88af4e7a8 | -14.80151 | -48.81011 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c28e832f-0f54-32a7-95c4-208275833cab | -14.80068 | -48.81495 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a8200ade-35bf-386c-b71c-0216a87ad511 | -14.77168 | -48.04453 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 63b7b5b7-bc06-3e99-9ccf-09c210df7bb8 | -14.76594 | -48.03477 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f270d82c-6380-3e02-943e-d97a7a48dfc6 | -14.74529 | -48.80048 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfef37a8-dbbb-394b-a385-e2f33758d8b0 | -14.68997 | -48.7827 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08b9188b-895f-396b-8e40-67c64215f0b4 | -14.68704 | -48.77731 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 019cdc0b-d14a-3b66-9a52-a810fef12fa5 | -14.68621 | -48.78214 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dadf166-dccc-3b68-9313-b15db0410362 | -14.68329 | -48.77669 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72d16bf9-76c4-3a29-870a-da6ef33ce1cb | -14.67953 | -48.77608 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a7de648-2f44-30ec-a18b-8b938b17f99e | -14.67577 | -48.77552 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02ddbc3d-37d1-3e0c-bbd8-705276cbe07b | -14.67076 | -48.75993 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb138edd-10c4-32f5-b7c9-0591cf88adce | -14.66992 | -48.76479 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b69d760-c7ee-34d5-8874-5f44f0c86888 | -14.66699 | -48.75946 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 886f3928-21e4-393b-8a0e-6189d2098993 | -14.66616 | -48.76424 | 2024-10-05 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c906b795-72c3-394f-bba4-fa8b02d597b5 | -14.58199 | -48.82714 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f137cc9f-c52b-3a41-b4d0-8c035210efd8 | -14.58118 | -48.83182 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 396f766d-a2f0-346c-9909-4ced712ba75d | -14.57825 | -48.82637 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60aa4640-f0e2-3638-918b-5e94900d319d | -14.57743 | -48.8311 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d62679e6-82a9-32b8-a13e-2068ce58614f | -14.57608 | -48.81649 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 226a08aa-08ac-3019-bc7b-e5346e2ab299 | -14.5753 | -48.821 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 117b84fb-96d1-3237-a4fa-2b50ab12c80c | -14.57449 | -48.82569 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3526857-baef-344f-b476-e48c1343520c | -14.57368 | -48.83039 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7ccb581-6906-3893-884d-caca88a84047 | -14.57233 | -48.81579 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27acb809-5761-304e-bb82-8652591e0d57 | -14.57154 | -48.82035 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18913c02-7348-33fc-8438-f5d87a5c45b0 | -14.5686 | -48.81494 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 97a7197c-8785-349d-a486-07eab0cfbab7 | -14.56781 | -48.81952 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1566bacd-9d60-362b-979c-8f92854d85c1 | -14.56723 | -48.80052 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5185bc28-532a-358a-8a2e-f58764a2d700 | -14.56644 | -48.80507 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a43193bf-c76c-3e67-bc80-df3be58bd6ee | -14.56567 | -48.80951 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6640cbd0-dfd9-3ecf-90d4-942bd6cb69df | -14.56489 | -48.81399 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1fcd1275-b888-30ef-b964-a4a565d0f2f0 | -14.56349 | -48.79974 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 77c89310-1631-3eb0-844e-3315d54643ae | -14.56272 | -48.80422 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| efdb93ce-9b53-3ba9-aee6-093ab8e2cd13 | -14.56195 | -48.80864 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a47e49bb-2650-3106-89a0-20c021915351 | -14.56116 | -48.81317 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2cf807a0-bd10-3dc4-9c03-c026f95dfc38 | -14.55977 | -48.7989 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5075219f-3da4-337a-8997-4e67ace99d45 | -14.55898 | -48.80342 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ba091a1d-7d0d-37ff-9e3e-54749d98ac1e | -14.55757 | -49.29342 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d8241b2-27ca-3f95-a8cc-80c58e364bf2 | -14.55605 | -48.79804 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| dde7575d-bbc9-3373-ad38-be8550d22867 | -14.55526 | -48.80259 | 2024-10-05 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 284391ce-fafc-363f-abb1-4a5ab620abfc | -14.55454 | -49.28806 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63c35c40-be82-3252-935b-77936ccd8d39 | -14.54894 | -49.29719 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9f73b027-36e3-3e85-a243-21d5b18fce1a | -14.50418 | -49.27682 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a29ff29b-db83-3db5-9b38-c7fae5d1c33d | -14.50335 | -49.28162 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9357fda8-fa3a-3548-9ff6-586f101e2430 | -14.4755 | -49.28146 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9dea6c6-d446-34fb-a7ea-2db04ae4d31b | -14.47382 | -49.29097 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1a199fe-7281-3625-9123-d9541ae85389 | -14.47163 | -49.28078 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bab8a78c-9bd4-3758-ae23-f783050f0eb1 | -14.46995 | -49.29032 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cac239c0-6d7a-30c9-b578-92bf0a166b0c | -14.46607 | -49.28976 | 2024-10-05 04:17:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fd4ef09-66d6-307b-8482-9a123e84a019 | -21.92848 | -47.5638 | 2024-10-05 04:17:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b7e684d-4e43-3b53-986e-359574d710be | -21.77858 | -47.04269 | 2024-10-05 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bd41eaa-4d0b-37c1-8e26-d12bcd37c2b5 | -21.77799 | -47.04643 | 2024-10-05 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be5524e2-322d-3ebb-92e9-0b05f1eb549c | -21.77525 | -47.04208 | 2024-10-05 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 544dff7e-c1b2-33bb-994d-c2fa5b4267fd | -21.77465 | -47.04581 | 2024-10-05 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e42009f3-9c5b-3ea5-9efa-d9a31b16af03 | -21.77192 | -47.04147 | 2024-10-05 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 358b9d20-2071-3525-a57d-f5dfcd3850bf | -21.77133 | -47.0452 | 2024-10-05 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 401bf8d5-6ec2-3d2d-88bd-6e7a9f629a40 | -21.2881 | -47.39781 | 2024-10-05 04:17:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b368ad11-95ee-38f0-8b0e-34b8bb7e7eae | -21.28476 | -47.39718 | 2024-10-05 04:17:00 | NPP-375D | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac862951-677b-3656-b354-a5299a2590d1 | -21.27683 | -47.40345 | 2024-10-05 04:17:00 | NPP-375D | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0519f5b0-65fc-3825-b45a-cd63b3fcd80f | -21.07822 | -45.72553 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c786bc53-6a1a-380e-8cf4-c667b9468f73 | -21.07765 | -45.72927 | 2024-10-05 04:17:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fca3ab6-5ec8-35a3-8ccf-df786c950ce7 | -20.91074 | -47.01097 | 2024-10-05 04:17:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eef76175-7d37-3766-a5f8-3f36187f8c46 | -20.79875 | -45.42955 | 2024-10-05 04:17:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4a433dc-34db-3d54-be35-0984558826d3 | -20.79232 | -47.75673 | 2024-10-05 04:17:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2ecc4c3-35f2-3ee3-9d17-b17a055adda8 | -20.79148 | -45.43213 | 2024-10-05 04:17:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02ae3ea2-4336-32f5-b36d-f686adcbf81a | -20.78894 | -47.7561 | 2024-10-05 04:17:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README78.md)
