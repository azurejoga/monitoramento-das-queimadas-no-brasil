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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 728016b3-cee5-3c8c-a266-bf3eb829f3ab | -5.389 | -45.93541 | 2026-09-21 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ba16aa5a-698b-3749-a1f0-c6b0da23ef6c | -4.5753 | -42.94466 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 751a249a-d7bd-3a88-94ed-98c5dc46f7f7 | -3.30606 | -39.28571 | 2026-09-21 16:03:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f522e634-bf8a-3ef1-9cee-5bd728edffc0 | -6.80275 | -47.89841 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c8dd9d6-068f-3fd8-8d84-0872ad479a7e | -6.5349 | -44.86813 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ed96b1a9-1221-3940-8190-67b98a594a43 | -6.08384 | -38.30305 | 2026-09-21 16:03:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b95b2c1c-d292-334d-991d-4e5911a18eea | -5.99251 | -41.0462 | 2026-09-21 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9d8489c3-5df7-3257-a1b3-8752f18a8b18 | -6.88792 | -41.70943 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 7149d360-5da7-31c4-9ba7-b7638f736192 | -5.61598 | -43.38742 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 49b155b2-7dea-3459-82c4-bf83189f3c63 | -3.7842 | -40.13212 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| e95b114d-605c-3fba-8bfc-75a255390ab5 | -6.15698 | -47.49726 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e69a8464-d1e9-3ec4-bf3c-d357afde5d13 | -8.32137 | -46.00627 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 54154810-faeb-35aa-89fa-8890dc03d241 | -7.62135 | -46.11974 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14fedbf4-f838-378c-bdd8-f2297b1a3109 | -5.7685 | -43.70028 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ebc74f83-0076-37ed-bb63-e2ff81cef146 | -6.22579 | -45.44398 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| deb075f4-bd7e-389c-a0ec-184a12e89731 | -5.58406 | -45.55721 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| e4471749-5bd1-3811-a1df-664ea6d63422 | -2.61956 | -51.72948 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1a2b6fef-7e58-3382-96fd-8afbbd45805a | -5.65841 | -43.42105 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 143399c6-1ab6-3bc8-851e-5c09299c4733 | -5.57828 | -45.71851 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e84002f3-4d88-38c8-b35e-49457127f218 | -6.22509 | -45.43885 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f3a15818-709a-3ebe-a3ed-40f91b32d64f | -6.32029 | -47.62071 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19251a2d-1fc6-3f44-bff4-ec4213d6bf48 | -6.4287 | -44.91161 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41dbd2fa-dcb5-3594-8e00-adbd38bd939e | -8.41591 | -46.869 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4a33eed4-dec8-3ca1-b29a-268cfbde43d6 | -7.1105 | -43.56855 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3d2ef498-a231-359c-b727-918b7629f12e | -8.4193 | -47.53324 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e481654-902a-39ef-bdc5-c1ecbaabfd10 | -3.42721 | -39.54679 | 2026-09-21 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f4c28b63-d419-3e08-a32a-a935cd3501ac | -4.949 | -45.15485 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2e1542b3-4f73-35cc-81e5-6c7ed5ee5aae | -5.97138 | -46.03574 | 2026-09-21 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 666f2428-20cf-37fb-a62a-03a2aa63edc8 | -6.18898 | -47.60685 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fb22aa6e-3d65-3b30-98c6-bdd030c0e1bd | -3.38764 | -42.86496 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92e7cf0a-3473-3066-b896-33c748f985dd | -8.61949 | -47.3036 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9e11e84e-e74f-3984-98be-b4d5303cdea4 | -6.82859 | -45.56389 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c9369ffb-f3bf-374c-81bf-3d351e648831 | -3.78463 | -40.15781 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 72b5045e-bb8a-3678-9adf-166a9f1a47e8 | -8.81112 | -48.75629 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 51e5ad94-c31c-3e7d-af22-138a41ea543f | -5.34904 | -45.9603 | 2026-09-21 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b74ebe4b-63f1-380d-ae47-2f410098ffbd | -6.46418 | -45.16293 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b6fb146-09d8-322d-b936-101121c67bf8 | -6.18611 | -47.49472 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4b75bd79-7015-3d55-9d21-69b96c5f2e13 | -5.58805 | -45.55155 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 05adca01-2e27-36f5-8df0-159f052e1d7e | -7.97427 | -44.07982 | 2026-09-21 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2121f05c-ff05-3836-a597-1d95101f2cd5 | -4.50796 | -44.96539 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d575386a-6c28-32fc-bc42-0dcd9cf16cfe | -3.33814 | -42.7654 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 0360ce7a-c789-38b5-a0a0-87590f4f2daf | -6.15795 | -47.70579 | 2026-09-21 16:03:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 68182c20-90e7-3ba3-b671-85df55110d20 | -6.25876 | -41.65924 | 2026-09-21 16:03:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| a77af680-7c6b-32bd-a5e0-100e83f78a5d | -1.51124 | -46.8443 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 579a5523-1426-3bc4-9381-b424f8934af5 | -3.25064 | -42.80159 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 913daeab-9f39-38f7-ad48-18769e8bb673 | -4.05885 | -45.67889 | 2026-09-21 16:03:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 91e3422e-f9ac-3aff-a9ba-fd5515520b04 | -6.8176 | -43.72806 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7cd023b3-4600-351a-ba87-6dcd5ca09cce | -8.797 | -48.74325 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 78bc355d-2be6-39a8-a892-eb30c48a97b1 | -3.83082 | -40.69778 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 81655a74-0252-35a5-92ea-40835ac285ad | -8.31791 | -46.01878 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| dd22d83f-93bc-358f-bedb-b9a48e88203e | -3.34711 | -42.77347 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d0723b5e-1324-3b9a-987e-89b23ff4c2fe | -6.79139 | -43.91108 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1152ddce-7c98-35be-81c9-0ab9c0a34d90 | -6.63646 | -44.82307 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c78159ce-2ad8-33d9-840e-dcb890056469 | -4.14073 | -40.61406 | 2026-09-21 16:03:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 02d70fe6-25b0-3376-ab23-88403520aef4 | -3.32515 | -42.55365 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9590f1cd-2ccf-33e3-aa23-3a553c9e4334 | -2.62173 | -51.72538 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 6b4354e6-6cca-3d02-8470-7ee311618031 | -6.46349 | -45.15805 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b72794bf-739b-398f-b792-598846418d2d | -7.6279 | -46.74286 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5242f51d-8b42-3482-9fe5-1ca54571aa25 | -5.54027 | -43.18136 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a644b06c-530e-38b5-9a66-7320c35652c2 | -5.83427 | -43.86295 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 10b3068b-13ff-3042-9612-2c8f777f1767 | -3.57757 | -40.31844 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b33d10b6-2249-3bd5-ac6b-841f1ad35a3d | -4.84951 | -43.55452 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 91ccc007-8da1-3781-8698-7080fc9121f2 | -3.59369 | -39.93143 | 2026-09-21 16:03:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 247fab76-a896-3d1d-bdf8-40d5b44db75b | -4.19894 | -44.79519 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| ba28d86c-bd68-3f06-ad13-d5be8a2c1822 | -5.79429 | -43.76247 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6e6b302d-c654-3274-9127-8de5e0ad6a88 | -8.30924 | -45.99284 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3acc7064-decb-3d2a-936d-6c05370481e3 | -6.64102 | -44.82251 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3e6bac1a-5bbc-3c21-b53e-c6e09f06aec0 | -8.49813 | -47.03024 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e8a6442e-c596-36f5-997a-c8aa8263e4f0 | -8.8031 | -48.74239 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b663dd6a-0d35-3b7e-b781-3a1e903cb8c2 | -6.39472 | -45.19935 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 354de257-6f50-3439-b6cc-57cbc6030cb0 | -6.60774 | -45.92009 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2c8f45d7-a08f-32ae-8503-558f090dfc7f | -7.05912 | -49.91747 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ca5719a6-806b-35a5-8e7c-e70aa7d55cb0 | -7.57372 | -45.43586 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 76e6b60e-3e32-3a60-af87-1ed5e7701733 | -3.33254 | -40.22656 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0477b26c-f990-3aef-8a33-b7c3d4fcca8d | -7.56181 | -42.65948 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c2f66319-646a-3c99-b253-943c94af25af | -5.82951 | -43.85965 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1f4ef7fa-5f0d-3263-971c-624ab449c371 | -5.23921 | -42.71322 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 8856d13d-b545-363e-b9e5-ae51b03019a1 | -7.57826 | -46.37256 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e021eaf5-62c9-3184-95f8-681ea6f828e4 | -5.31051 | -44.48261 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf5c685f-3598-337f-b34a-29b1d0609c31 | -6.93475 | -43.09682 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dea5abe8-3840-3ab4-b052-f7b77cbd2f12 | -8.31223 | -46.854 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d1f5393-25d0-3b6e-91f9-774a9bbbc663 | -7.36557 | -44.70955 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d261736-5394-3a75-8789-f82cf81fb406 | -7.03124 | -42.07655 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a0a3df9e-d87a-3d00-aadf-2897092aaeeb | -3.43269 | -42.85369 | 2026-09-21 16:03:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4d4ef2a8-43e3-31bd-a4c8-8e8443769678 | -3.38534 | -42.9734 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8a896ac6-45e1-3700-84da-efb5fbbb081a | -5.75682 | -43.7216 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c38b7212-bcbb-3737-b78d-3081fbee4089 | -7.33997 | -44.46024 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ced44c33-383a-37ff-b301-a2e80fa5bd40 | -7.73547 | -43.90731 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 7cf66cf0-8c37-3460-a5dc-51cb164ede25 | -5.3931 | -48.96096 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4f9400d6-2cba-35b0-8d5b-5d79ff6763c1 | -8.45468 | -48.44782 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c334d10d-d088-3254-b1ea-bea2a76b4046 | -6.73833 | -46.62231 | 2026-09-21 16:03:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a932d9fe-f1c9-3719-9c20-e672fb00c551 | -3.83848 | -38.6492 | 2026-09-21 16:03:00 | NOAA-21 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1cdcef00-d6ab-3430-b991-197e788585e3 | -3.2644 | -42.5305 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ffa18398-ea6e-3509-bacb-63e4a3b24d05 | -6.83544 | -43.76185 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0ebbdd07-4599-33c2-90c6-78e50b0e4b49 | -4.52679 | -43.88163 | 2026-09-21 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51d05b58-810d-3ce8-a3de-fcc0a7f0f47c | -5.99606 | -41.04566 | 2026-09-21 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e57ce238-54fa-3632-bbd5-e93d18fcf6f4 | -6.92083 | -35.3539 | 2026-09-21 16:03:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 958131e7-22fd-3909-a5d4-64c315c5383f | -4.31442 | -43.90929 | 2026-09-21 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 81384359-fa2a-35d8-9ab5-973755f2de66 | -5.82613 | -47.79177 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c68eb6ab-1d42-38c3-89a4-9b96d810d369 | -7.07214 | -44.31411 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README167.md)
