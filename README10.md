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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b44c76a8-49b1-31b8-aeb2-e3bd40ea0cc6 | -10.32919 | -45.22804 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c971328c-8f39-3bf8-8c18-5e729a6a6bdf | -3.5961 | -47.52045 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be8b2b97-d687-328e-93c0-b2b7df446d99 | -11.48648 | -43.58567 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d5ffa2c-60ba-3bfb-b792-ee65c44e9bf6 | -6.84817 | -44.17077 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d82e6366-6aa1-31da-9105-e83fec2eefec | -7.82798 | -45.62662 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1454e961-5cd1-3957-8e3d-54d3fac18880 | -8.48454 | -39.93033 | 2025-09-21 04:08:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5185f8ec-45a8-38f9-91ce-f77d456b597b | -8.01855 | -45.72255 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a2a7700-8508-32e6-bb43-00b430c4cf40 | -3.37242 | -50.39512 | 2025-09-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e005e8e9-4577-31f9-b7de-6cb14fe50df1 | -3.60501 | -47.52183 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71416239-6155-30b9-9656-de763ea8d20f | -7.93197 | -44.09378 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fc28cb8-5be8-3993-8392-e11f4437880f | -9.93293 | -45.59724 | 2025-09-21 04:08:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fde0dd10-4327-37c8-a8fb-7df80fa9aaf1 | -3.75885 | -54.81953 | 2025-09-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 89361b90-96df-3a55-b1ac-0c1520e55cc6 | -10.78231 | -47.32983 | 2025-09-21 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5ff0748-9233-38e5-aaba-c2382dbb26ec | -6.56332 | -43.46876 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79c65f6a-be67-3b60-886e-06ca3644f4f3 | -10.36885 | -47.90784 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fa35bc5-479c-3acc-b5ee-5ee6d6205561 | -7.72153 | -44.4543 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25ccdd56-452f-3264-a13a-a3b11fa79c61 | -5.09265 | -41.13851 | 2025-09-21 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c469920-4d63-3c52-b8aa-5fec5f09369f | -5.64856 | -51.46812 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52cfcc3d-a365-3cb9-b536-e6ad60531b2e | -7.19261 | -43.81941 | 2025-09-21 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab03b449-99ce-3071-b9f9-0912deba13ba | -6.07266 | -41.00336 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| afa7838b-ba93-33ea-9733-85d306ce8551 | -9.75982 | -41.88375 | 2025-09-21 04:08:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41401bd0-bd64-3033-831d-5117c2389d0e | -10.36315 | -47.89206 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f52d623-0b56-3bc9-9182-a20156104a0d | -6.67627 | -42.43005 | 2025-09-21 04:08:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 58464828-2d16-3a84-8a11-c01b3cb93e97 | -3.59681 | -47.51605 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8391f0dc-c6df-3960-b36e-6dd80ae47633 | -5.58968 | -51.19619 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ba14e09-6819-3029-b2a8-53ae7f32c5ed | -8.46347 | -44.71215 | 2025-09-21 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fdb34158-e697-3fa1-bbb9-8ae976ced4a3 | -10.28713 | -46.08114 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4d3c8951-bad3-30f7-8366-81fcb2e3d0e5 | -8.73415 | -40.5491 | 2025-09-21 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e8fe2e9-b5f6-314c-807c-4a09d058b431 | -6.3301 | -44.04983 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5678806-affa-34af-800c-fca6c6cfebfb | -4.41812 | -47.96738 | 2025-09-21 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44fb5ea6-5aee-30a1-8023-6b5faea635ea | -9.77142 | -45.95288 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91a6c802-d278-3b8b-a30d-43709b6e1f8f | -6.17006 | -43.68899 | 2025-09-21 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d94b3739-a420-3dc8-9afb-1e762c048905 | -3.81283 | -49.1055 | 2025-09-21 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6df6b539-79a2-3a9b-9ffa-fee184664575 | -6.087 | -41.0233 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2334a783-48bb-3781-b0ea-6a4c6b886f01 | -7.03843 | -44.54335 | 2025-09-21 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 877580f5-159e-3fe2-a23e-0b05a57407f2 | -11.47829 | -43.5517 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86d1c453-e0db-3877-b43f-85a5454f5278 | -11.48436 | -43.55631 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ecaadd3-8d52-3afe-a59c-a761bad457cf | -6.70811 | -44.01068 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81c31b90-1b70-325f-9129-6659a6c0ccdf | -4.94636 | -49.92875 | 2025-09-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4120c67c-b302-3974-8249-e7396f0e54d0 | -5.58773 | -43.79287 | 2025-09-21 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edd372bc-1b5d-355e-80d3-d677856816c3 | -10.366 | -47.89991 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98d8bee5-932f-3866-8cf0-e24de3b154da | -6.08977 | -41.02726 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 227cf53a-2234-3c0c-9eef-9798cf40a9bd | -7.9164 | -44.10285 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a652164-a01b-35b0-a3b4-ce6e57eb2b1f | -5.47509 | -45.37666 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f2db9fe-8590-3545-aaf9-53a31445b411 | -6.30612 | -42.36034 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9aca1fd7-8fe1-3c09-b855-6c4a420e24eb | -10.57244 | -48.59165 | 2025-09-21 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55b3684d-9586-374e-aba5-056b13b728f2 | -6.7321 | -43.02436 | 2025-09-21 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21a66814-c34e-3b61-b70a-018909318acc | -6.66881 | -44.8582 | 2025-09-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b687ca0-ea79-33f3-8f7c-bd37eca00f3c | -7.72374 | -44.46266 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f2933b36-266b-3c59-9160-1e603996a9c4 | -7.18257 | -42.23995 | 2025-09-21 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7c30f0f-d6a4-3ced-a435-30f102a5f041 | -9.42289 | -44.71206 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8334811f-483e-375c-96fa-b200cf9338c8 | -7.37071 | -44.57767 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea2f777-90fe-3466-81c2-d4919175084d | -4.5654 | -41.50244 | 2025-09-21 04:08:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b9949b3-6e50-3ccd-9a9f-3bb9ecd5785b | -5.41997 | -43.26203 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| edd1c674-2217-3de4-b25b-0b22120f364e | -10.28145 | -46.07265 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25789de7-9a0e-3b9d-8ba4-e6805d96c3df | -9.16459 | -44.61961 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62a03f82-7f86-3e49-a266-bb4c41026bf6 | -3.80426 | -47.57355 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a46f0738-fa69-3d29-9d34-2ac83c7e8916 | -6.5494 | -43.53463 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c70d76bb-5384-3086-908a-ddfae657fe01 | -6.25171 | -44.09261 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 606a8d7e-0485-3edc-a082-c4e65352ebc8 | -4.91279 | -43.09288 | 2025-09-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0e4731b-cdae-3705-96f9-5f80eaba1c1a | -3.60055 | -47.52114 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11184f2c-52fa-3f13-a516-699755a48f08 | -6.01634 | -44.33216 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 852916f0-1bff-33d7-8cbc-0097c3ef1690 | -4.68115 | -46.46462 | 2025-09-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afac4e52-42b5-382a-a7ea-7faceaba2961 | -7.56971 | -44.73631 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d165c4b5-4264-38b6-a013-3faa28f03166 | -5.79869 | -50.19978 | 2025-09-21 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7649684b-d790-3331-8266-47393d3ab95d | -7.35087 | -44.56313 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b526465b-a1cd-3004-819b-4609d840afc7 | -7.47841 | -44.38055 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f1974dc-73d3-3af3-bb0d-f73b5569a6e6 | -10.30029 | -46.09253 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85d540c3-59aa-3805-970e-82a6c19db16d | -6.67608 | -38.50179 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 53a37385-c457-3669-9f2b-b49bb309df5c | -5.35037 | -45.00531 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e70eed1-0d9a-3db0-9ec8-6b497f3adc35 | -6.554 | -43.53141 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246d4bdb-8386-3383-bbd4-9839c8b8ce53 | -11.21084 | -42.19681 | 2025-09-21 04:08:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b85dc27-7233-3775-a6e8-48b4739f8a09 | -7.83311 | -45.61844 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 777e4451-9a9a-37b7-a6ed-1b4ec29d342a | -10.32567 | -45.22752 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d30c598-425d-3d11-bacc-f2e1156e5ec9 | -5.69463 | -51.73597 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4234bcc3-a75b-3a4f-85ab-6d5e0c246a01 | -5.52602 | -43.86603 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c06571a5-79a1-32a3-9d58-ef7d0c368b81 | -5.59019 | -51.1924 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de7e4d68-249a-3541-9bd6-25566b26aca9 | -5.34014 | -43.3638 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d9193ff-4936-33e5-9c6b-776fb8c0cf57 | -6.55339 | -43.53149 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fe04bf3-66f1-353a-a632-6caa41a1508f | -6.38895 | -44.62854 | 2025-09-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b4f831-219d-3eb5-ade5-cfb8566eeac5 | -5.63564 | -45.95892 | 2025-09-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50606e8f-4436-3df3-a3ec-a5e6317364b9 | -11.4634 | -43.53841 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f22d71-c25f-3ab8-8171-93986e27d622 | -9.42763 | -44.70493 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b92a8400-be72-302f-a1b0-e5c1f7129c7b | -5.75755 | -42.57801 | 2025-09-21 04:08:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 937d3b5d-d234-356e-87bd-55b13c482235 | -7.92892 | -44.1126 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11acda46-e032-3d44-b759-5c43d9af6eb9 | -7.94449 | -44.10351 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e019d0ad-e081-3bf6-9da4-b624d5690e54 | -7.38515 | -47.04786 | 2025-09-21 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1c4a9f8-4309-3c10-ae79-e4d9d49f352b | -9.43109 | -44.70554 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8536ca0d-77a6-35e9-b967-6cad47814be9 | -7.72438 | -44.45876 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 748b4ce2-59f5-358e-9d54-ee7685dca052 | -6.01346 | -44.32756 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0acfa73a-706d-3d59-aa42-108fbad37af3 | -6.3122 | -42.36482 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd302643-3f81-39e7-b9ca-730e7e5930ad | -11.48711 | -43.56038 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 591dc81c-f3c5-3953-9431-2373d6ebde5f | -7.18202 | -42.24342 | 2025-09-21 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52d000dd-78f2-3f38-8439-d167dcc325d2 | -10.34337 | -47.88477 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd0f6b74-99a5-3878-968d-8688f1d0719f | -6.49052 | -44.38467 | 2025-09-21 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1744c29a-609f-3a09-85a3-609acadc9db6 | -7.91746 | -43.88043 | 2025-09-21 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9270f088-45c9-3fbf-95a9-65a9a0d79092 | -6.31164 | -42.36835 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 040b3229-f10e-33e7-9201-594527039abc | -7.9354 | -44.09433 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e981828f-91b1-3657-9e69-0b4d16415f0f | -9.17153 | -44.6207 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e39b99bc-039a-39ce-8b59-2e857f2e6010 | -10.35438 | -47.89408 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |


[Clique aqui para ver as próximas entradas](README11.md)
