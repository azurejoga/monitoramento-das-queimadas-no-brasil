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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dfd2141-79c1-3e8c-b8df-7761bfbda754 | -3.09625 | -54.29171 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58a43b4e-97da-35bb-b5a6-fe697ba1f505 | -2.58379 | -56.15639 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04340fe8-20f5-3542-a35f-8019169032c5 | -3.04228 | -54.25936 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 983176a9-67f7-3801-aa7f-db8fd76cccbd | -3.04534 | -53.9549 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 793ad679-0f86-33b1-89b8-79713829f8b1 | -2.22505 | -58.11242 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb73f09c-334a-33f3-8a8e-f90950f6f868 | -3.05087 | -57.48577 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7b27f89-eb42-316d-8386-00f7515ad321 | -3.01214 | -54.10285 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bed88bb5-09d2-3422-a93c-b8deb9b658a9 | -4.80876 | -54.6781 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2ca687-7346-3ac8-b528-e6e98274a03e | -3.0494 | -53.92801 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa3a26e7-570f-31ea-9478-c00c046e8774 | -3.02995 | -53.91113 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3716c08f-cb7d-372f-9c5d-4fee324553b3 | -3.39053 | -59.59288 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c732271d-b9d1-331d-aa3e-06094b7b6165 | -3.2612 | -59.60611 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19b0b99f-9c0d-37ff-bfe8-0746517fe0f8 | -2.9582 | -54.13791 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f7c5023-7d88-396e-b1c1-6571216a1fb3 | -5.2998 | -60.08784 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44b13691-fcaa-35a2-b5df-9974e957e66a | -3.0204 | -54.08405 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76697d3b-ada9-3c7d-b6a1-a7fcf1e6a0ad | -3.05487 | -54.21269 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5edbc40d-0aba-334e-8904-40e12b37c364 | -3.27373 | -54.04378 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56607e6c-8b7a-3730-8a20-09880e1098fb | -3.93324 | -54.57766 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fb1f906-14de-3770-b7ed-8cf0f9267b7a | -3.16285 | -50.59716 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6181f8b-5345-3b3d-814e-b7bd3e63ebc8 | -3.98337 | -59.34221 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b63f7ec-98db-30d9-8a27-3028ff50885d | -3.84877 | -55.9808 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6e1daa6-4197-3a9f-bb51-83d28933bbe5 | -3.01325 | -54.05932 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd37d4da-8795-3cad-818b-acf12b0ebd34 | -4.91865 | -55.86328 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4444da8b-0fcb-3388-b5c9-7a67c1320656 | -6.16138 | -52.65525 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbf45a83-c813-3443-bc35-e42488346e31 | -5.29045 | -60.09393 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b22bc501-a794-3d19-a0f4-a65f4a3fa4d2 | -4.80828 | -54.6813 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfaa170f-d8d3-30f3-b6e7-505b69992ee0 | -6.1446 | -52.64632 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b340b62-ea74-3240-af30-ade1e48d4eb6 | -3.02707 | -54.11175 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 244b86aa-e90b-3325-8482-ca9427b08899 | -2.76927 | -54.07509 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8577daf3-8434-30bf-9129-730ec67270dd | -3.28365 | -54.03507 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d386f3a-2b3f-3255-9162-44c25d7de4fc | -5.74473 | -53.46018 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177215f0-efdf-383a-8c3f-7087004f625d | -3.05019 | -53.95907 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 8811bcfe-2ec2-31fb-b704-e11b75e79d28 | -3.49868 | -59.27277 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 365112ed-2d73-3aa5-bea4-7a30821224dd | -3.0777 | -54.27229 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8557fd88-bad6-3b30-87d4-3d4f5bf3ff85 | -6.22835 | -55.61954 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3520a966-a3b8-345e-9fd6-591a967a94c9 | -3.11558 | -53.79408 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 874bb0be-0b8b-3d62-b4a7-a068ac99ebc6 | -4.42486 | -59.49168 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fd394b1-4553-3eec-87e4-9e70a5131fe6 | -3.01127 | -54.07253 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f19fcbf6-d712-31f9-9142-8ccbd51aa85e | -6.23341 | -52.85543 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68fd42b5-9ec0-3b42-a9e2-a9cccd0b94a1 | -4.26496 | -54.88059 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 440cd969-30ab-395b-b29f-b168a1e98523 | -3.31377 | -54.05338 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c339568c-d853-3240-9439-b26998c75136 | -3.98416 | -56.22538 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0217e9a-1855-3633-b597-836d00df424c | -7.21882 | -55.16973 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49ad1ff7-0491-313d-9ceb-ac778bc9db15 | -3.05853 | -54.22026 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df8c6379-b3b5-30cd-b319-8fc22c873aef | -4.42786 | -55.16557 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14eb8c15-6e4d-344c-ae61-97edd7bebe23 | -3.28822 | -54.05623 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78ab5392-6781-3e82-8bae-2b08d5632cb4 | -2.46661 | -56.0642 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93f667b4-db4b-3e78-adb9-65e9a6157529 | -2.99345 | -54.04613 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e775ac82-5b4d-350e-8dc9-308a3b63aaab | -3.29053 | -54.07679 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32f4b35f-79e9-39c9-975c-5833eee55c51 | -3.00595 | -54.0717 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 28073a72-ac30-3341-8cb8-6dc751fb77d4 | -3.96125 | -56.12236 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10acf3e2-71fb-32cc-ac98-802898b5f7d4 | -3.17157 | -54.74706 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b1fc147-0a08-35ee-90a0-0d1897e8eb8e | -3.30834 | -53.86477 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d33c70bf-d528-3f94-a526-349a55c55101 | -3.50246 | -59.27335 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fc6e2a5-978c-3ad9-839e-33afdc60fd7b | -3.28753 | -54.04599 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 468a8aa1-aab7-3466-9872-42d0deab4d68 | -3.0818 | -53.94999 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5c806c5a-8fd1-3f65-a2db-814998dc7dd5 | -3.54194 | -59.49883 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e379df0-9e8b-381f-a4ff-5f774147654f | -3.49742 | -59.53033 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c0ec4c-bc85-34c6-a139-ca4823d31948 | -4.92911 | -55.8595 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c077b5b3-88e8-3dcc-bcca-93ebd88e63e3 | -2.8634 | -54.1623 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d90b383-af09-3705-b1b9-e2f6f04d9a2b | -3.16688 | -50.59582 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| daefb0cb-c7f2-3387-ba6c-c0bf1a38da6f | -3.58209 | -55.60541 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 664f5427-cd20-3dd1-a4af-db439719ceb1 | -3.03714 | -53.93648 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0809d185-5895-337e-b728-650d4f770eb7 | -4.29115 | -60.96011 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83714e22-71ce-37b8-934f-f9d73553294c | -4.56543 | -54.95671 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b169caf-ee7f-3832-ada5-563a187a5bd6 | -3.51292 | -59.33089 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57bf2386-2eb5-3a53-94a1-887f8717ca77 | -7.22246 | -55.1036 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c37a76f1-25b3-3fd8-8e1f-7f9219f26b7b | -7.21926 | -55.16649 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1284f091-6ba0-3000-8c4b-245be581a3f5 | -4.30032 | -50.78963 | 2026-10-08 05:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 736fc9b6-9d97-3a5a-956b-4bdcf449ccc1 | -3.3026 | -54.05503 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f1b58d9-3579-3d3b-82e0-55ac3d084126 | -7.00823 | -59.12195 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 76aa2cca-17c3-39ca-9e92-36667828963f | -5.68841 | -53.47932 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a64ac23-1110-3e63-9827-f3a5b73facf5 | -2.98897 | -54.1128 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0af83ff0-4ccb-38e7-ba71-ac6cb226fd01 | -3.2674 | -54.04948 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd05ed8-ba2b-3d41-b2a4-b6447d46e042 | -3.00437 | -54.11854 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 161b60ac-10a7-3ce6-9310-5e49a164e384 | -2.4949 | -56.06367 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 852b2f1e-5683-39a8-817d-c66c987c2b76 | -2.58166 | -56.17039 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff3cfb2a-a929-36e0-893d-5dbe267d036d | -5.07288 | -56.90546 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd0ee3b0-f552-33f2-b5ed-fac54677b19f | -2.82404 | -54.10666 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e4a34de-f6bc-3662-ad51-994ecc01246d | -3.51808 | -59.32238 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f99097d-5140-32f5-aea8-f3ee963e0034 | -3.00818 | -54.12917 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b10bd14c-11df-3693-92ee-5d459425be29 | -3.53559 | -54.66105 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64fb20d8-e4b8-37fc-9468-deafcbcf0f3d | -2.49876 | -56.06917 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 37e96749-8ce5-372f-929b-f8afb6778421 | -2.95337 | -54.13394 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96dee022-0ba2-30fc-b82d-b98479eb7d55 | -3.04609 | -53.91351 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a514c67-a931-3cec-9621-541a6e4a2096 | -3.02522 | -54.08812 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 939d1d10-6b33-3672-a648-0d20df4e22e6 | -3.43525 | -59.53897 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9dd031c-6193-3317-a581-7398fa6c4850 | -2.83639 | -54.1318 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9051fea-ffef-348a-b947-950fd6ddd8fc | -3.05421 | -54.21301 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6122a14c-3831-334b-a913-7f570190f6d4 | -3.7234 | -55.48962 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4eaa7ea-2368-37d3-8b12-a3527efd1ca4 | -1.82829 | -55.0483 | 2026-10-08 05:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b28fa90d-ac22-353d-9921-f7e8e42173a3 | -7.89824 | -54.71579 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63261420-a69e-387a-bb42-5890a3972414 | -4.35657 | -59.94446 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88309c4e-b4f9-351a-ba14-61f956725598 | -3.03432 | -53.91871 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd3a919-562b-3cbd-9820-83ed6b80a351 | -7.89257 | -54.72216 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cfe1390-55bf-3e3f-803f-7309a0795b9c | -3.12788 | -53.70362 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 689a4a4b-91ea-3d29-b194-992a0ff38741 | -4.12347 | -59.88356 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43ace7c4-46fa-3ffa-b78d-4de3b3cfc2e4 | -2.93812 | -54.16743 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 466d3134-470e-35ee-9ebc-9ecb2146373c | -2.15441 | -59.22253 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e514f1a-dbab-3936-8998-08113f6fa46b | -3.18361 | -60.05835 | 2026-10-08 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README195.md)
