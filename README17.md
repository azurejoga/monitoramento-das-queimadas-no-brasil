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
| 725a4607-ea5b-331b-b16f-24fb1d3aee24 | -15.77284 | -43.13334 | 2025-09-19 03:55:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 90595209-517b-3a6b-b98a-71fb2b31a21a | -12.89769 | -50.5498 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 739f9658-f848-3115-807d-76ea2f0484ec | -10.2944 | -50.22855 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 91e9c500-096c-3610-b96f-617514c254e0 | -12.8878 | -50.53895 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce061223-1d13-328a-ba6d-26d625dc12dc | -11.45 | -43.54774 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e782db9b-d0eb-3562-9af7-7e6c20394fe3 | -13.2207 | -44.55537 | 2025-09-19 03:55:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80bfbe5b-78d6-36e7-970c-a3c4dab53c54 | -17.11641 | -43.59663 | 2025-09-19 03:55:00 | NOAA-20 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dcbf1fd9-56a6-3882-adf8-39611c8ec541 | -12.9117 | -50.57032 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30f1a8c1-ae1a-31fa-bd47-78a8cb7f667c | -10.87924 | -45.43935 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de881132-9af9-3db4-8fe1-43f297740231 | -10.28426 | -50.24947 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb7efdb9-1812-3ef3-89b2-303442246226 | -11.15931 | -45.33425 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d196e71-113b-3817-a04f-7412d67a6cd6 | -10.29754 | -50.22824 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 7899b246-50f4-301a-8990-ca164fec0344 | -17.35177 | -46.80966 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12edcd15-8f6a-33fc-bc86-86f1cd63a944 | -10.66801 | -46.44606 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0b13b77-c167-3268-9fff-ef0d0eccb9a7 | -17.34632 | -46.81536 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67c07257-06bd-3e60-a33c-c05d6621b9e4 | -10.29949 | -50.23419 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a2dfea2-001b-3d4f-b6f4-748449b66956 | -12.09552 | -44.81166 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ffda2fba-e395-3dbb-a390-7af65b96c889 | -17.20713 | -47.34697 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a653b85-4fd3-37be-b914-9c480187da68 | -17.21674 | -45.94603 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 855eefed-e921-33ee-a3ed-53c92605fb09 | -12.89525 | -50.53178 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 61b0bb65-29ad-3cf5-96f4-caa5ddb577c4 | -17.45648 | -44.79487 | 2025-09-19 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44bbb49b-27a8-34f7-a228-980abdf35362 | -12.09707 | -44.85013 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc3a0deb-2202-34ab-821b-145868766ce3 | -11.45834 | -43.54451 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1b19afe-716d-383e-aa84-f153167a1668 | -10.91933 | -45.64605 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20cc7033-e12e-3d7e-823a-4bbf7840b150 | -17.08682 | -43.34306 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c8748e5-a22a-3f89-97cd-0088deaa6097 | -12.47967 | -44.74194 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88262f30-51c9-3e27-8553-2336ac64fc97 | -12.09421 | -44.81908 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd3828ac-fd59-3453-8ca9-cb94afb8ae8e | -15.44757 | -45.44703 | 2025-09-19 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38f656a4-cbc6-3bfa-a6fe-0e1a0fab3f2d | -10.30347 | -50.22945 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 31b15507-cff4-378f-ac16-d8c403134f47 | -12.09029 | -44.8412 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cab9e579-98cc-39ae-b916-294d332cf53f | -10.24741 | -48.04363 | 2025-09-19 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae140dfa-fdd8-3d2e-8c5d-4431ba8c3045 | -17.45277 | -44.79415 | 2025-09-19 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80bd22db-7685-39f9-b2e3-705e8ea8e7f1 | -13.98112 | -44.96806 | 2025-09-19 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82721bec-e0f1-3ec9-acaa-a251e8914cca | -14.46783 | -44.8648 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db37317a-eec2-3bad-8fbe-ef8d68f7f5f9 | -12.9183 | -50.56739 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2722f38c-a6e2-3593-aebf-da3607d85885 | -12.54493 | -43.00219 | 2025-09-19 03:55:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9ee06061-84ed-3b25-94f4-2525fc66f34e | -12.15446 | -44.95079 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 796651b6-b88a-3b44-a9b6-6197e2ba209b | -12.93069 | -50.56569 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5937d18-470c-3156-baea-4afe03e36ab7 | -16.51501 | -43.54959 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 985ca652-0672-36b8-938f-73f84fe15bd4 | -10.91974 | -45.63854 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 030b3c5d-bdbc-3573-a48d-6f235246d118 | -11.20978 | -49.6404 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d5b0bc3-fc55-3252-98a2-a1de5ab717cd | -10.91856 | -45.65028 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49c28f86-71ad-3601-b5f0-1c813a05951e | -17.56818 | -43.79747 | 2025-09-19 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f98ca17f-e723-3092-9501-082fa92d978d | -15.7616 | -49.95093 | 2025-09-19 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c1cdbc8-dd10-3be7-8d8f-3d7982feaf49 | -12.90019 | -50.5372 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef2fa090-cd8d-3691-9e3a-932da76d3746 | -11.09035 | -41.06784 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 191751b1-3fa5-3409-a2fb-aa1b6d457771 | -10.91901 | -45.64272 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76c4c40a-5427-3033-b5ce-68c46238e4fd | -17.19235 | -45.89956 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9b43739-8e29-30eb-82d4-1c036113403d | -11.42019 | -41.40973 | 2025-09-19 03:55:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84b524a3-1b38-3005-ba41-24c7fb1cc156 | -12.08073 | -46.57093 | 2025-09-19 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dc168f3-db71-308b-a695-7ea15b2bebeb | -14.25825 | -44.70695 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aeb36b9e-7685-3963-a25b-cbd4e05485f4 | -11.20567 | -49.63146 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5cd796b7-7f03-308d-87d6-890b593c6dbd | -11.22179 | -49.63881 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab5634f6-403d-34bf-a250-436ff36f9390 | -10.70032 | -42.86382 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b3201e6-7dd4-3c70-b113-118c193cc5aa | -13.33553 | -40.46728 | 2025-09-19 03:55:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e2696ae-f85a-34ab-bbd8-c39e1bbe28d1 | -17.45569 | -44.79936 | 2025-09-19 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1fb8c33-76c7-34bb-b42f-183e63725386 | -11.21279 | -49.62487 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49795281-f5dc-33c3-ac5f-ef9b05a83ebc | -9.7634 | -48.57869 | 2025-09-19 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96d951c4-278c-36d8-96e1-efb0d9fe1eb7 | -10.29524 | -50.22412 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 7e9d749f-09f5-35cb-8bb1-58a5fe9f4002 | -12.10651 | -44.84402 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2006bc32-6904-32c9-8056-17e2543978c2 | -10.96304 | -49.57388 | 2025-09-19 03:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d411dbac-082c-32d2-ac47-763de45328e2 | -12.88864 | -50.53476 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 020bfcbf-4e26-3eaa-9716-ef54b8f17d72 | -9.73977 | -47.86389 | 2025-09-19 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cae4d286-74e4-3259-bfa0-b169360d202a | -10.24284 | -48.03944 | 2025-09-19 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfae7e10-0e52-35ee-8ac2-7b8e37bcdba1 | -12.47568 | -44.74114 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50f145b0-1c1b-33d0-b027-eae595f0ac78 | -11.33781 | -43.4777 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4f2dfc8-54c8-39f2-a55d-964638943b81 | -12.89852 | -50.5456 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ddd761e0-03cf-3c20-90da-a10f02998138 | -17.19334 | -45.89421 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0b1acaf-1bbc-3056-8c82-1e165cb412b1 | -13.14955 | -42.555 | 2025-09-19 03:55:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4edd0c8c-0b97-34fd-bd79-af3864a9e6d7 | -16.79762 | -45.89954 | 2025-09-19 03:55:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc1183d2-0700-3016-ae85-4577c49b9bff | -10.2958 | -50.23707 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8dde2784-ecf1-32d9-a7fc-58cb65614f70 | -11.2034 | -49.64313 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c44e5efc-2c74-32ae-886d-751b975d2898 | -14.54864 | -45.52986 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86c8fa3b-ace0-3a40-a7f0-fc5d46824e90 | -10.92113 | -45.6563 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1f19480-db4d-357b-98db-f8baa64311da | -10.30793 | -50.22213 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0f9d68ef-bed8-3cd7-97f5-22a2c55f4f2d | -12.88036 | -50.54608 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| be6583ad-28d0-3750-8e02-92b9b5b0e9f4 | -11.21691 | -49.63377 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd8405b6-4887-3189-867b-8d4ad21ed1ab | -10.2851 | -50.24504 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2e5b5d59-269d-3063-891a-315a2eda2e73 | -12.0842 | -44.82846 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fc95ee42-b8d0-34da-9558-222656cbfafd | -13.98426 | -44.99592 | 2025-09-19 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3baffa70-3f29-3cb6-b0c4-fac56da40626 | -12.11053 | -44.84491 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 328bd045-aad3-3aeb-ad7d-d7955df9c9ef | -12.07622 | -46.56995 | 2025-09-19 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e57df290-5379-39a1-bc01-7e6aa63855c7 | -14.35399 | -42.34168 | 2025-09-19 03:55:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee42da2d-ee7b-346a-81d5-55bfd83a59cf | -10.28987 | -50.23587 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 65537c30-48b6-3aac-aec9-8e1e19c7b562 | -11.45377 | -43.54846 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58b971ee-4c18-3883-bcc5-eacb94b4e177 | -17.17366 | -45.90113 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 724f8b93-34b4-3ef4-a0db-b33d466e2637 | -11.51385 | -40.63976 | 2025-09-19 03:55:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 845c3b88-aec9-3c8f-a4f2-bd39e1810d5a | -14.5861 | -45.17838 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c352af9-6c0f-365f-b0c9-375d8836d4ca | -15.52811 | -41.43333 | 2025-09-19 03:55:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 240e9788-8b5a-3f5e-b86e-72ced77e5f5e | -10.87148 | -47.78436 | 2025-09-19 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6957b853-1a75-30b6-b23a-423e081061e9 | -12.92475 | -50.56265 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5994a928-51ab-3400-8efd-556b30c66de0 | -14.69211 | -43.98705 | 2025-09-19 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b0d6141-b665-34b4-ba96-2722cf7d1615 | -17.2174 | -45.94245 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 795fb0a4-e04d-3294-b6d2-f67d4cacaec0 | -12.47629 | -44.73762 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0522fc5d-b989-3a97-aca0-f8d44be3cfad | -11.09096 | -41.06414 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9455cd77-22b2-3ec0-8db7-9e4f451d905e | -10.29356 | -50.23297 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 31dda8d1-fac6-34df-925d-862d9dfe2f62 | -10.79339 | -45.96564 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30b7f8cc-a7b3-3a05-91f3-9893d468cdc0 | -10.29667 | -50.23266 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6cb62498-f9a1-3187-9d21-c898a92923d4 | -14.64184 | -43.96846 | 2025-09-19 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e202bf78-f3d0-3520-8f18-7367135b66e0 | -17.22406 | -45.95119 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README18.md)
