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

## Dados Diários - Página 303

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf6ec8b1-ae2a-3788-821f-1a86ed16a62a | -4.45425 | -47.92171 | 2026-10-08 16:20:00 | NPP-375 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7f654f94-7f71-334e-b1ab-b03bf1b1f563 | -5.533 | -39.85505 | 2026-10-08 16:20:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 81e18076-b363-38b1-88e6-67e19899f38e | -6.94523 | -43.06902 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a3006087-b0e6-32f5-8192-6bc7aa453647 | -4.16262 | -40.77893 | 2026-10-08 16:20:00 | NPP-375 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 22b3f80c-6fa2-3b16-bb6b-6c3999b0d056 | -6.15603 | -47.94302 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 499532b9-0428-33a3-930e-fe77483e88da | -5.55682 | -45.61455 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 26d2e18f-1d2f-3c6c-8672-35f6a525d59d | -8.20993 | -46.41246 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 20e0d79d-b435-32e0-9ec3-4472428e1738 | -7.54282 | -42.08671 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| f5e13a00-1c4a-3a45-beda-a47684339b2d | -6.91635 | -45.88352 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54475fd9-8f13-3641-92d0-e83d114a033b | -7.54221 | -42.0826 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5bebe96b-4d8d-3d02-9068-048f24c3e83b | -7.53563 | -42.08777 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| b4df76da-e3ee-36ce-b1b9-96f2806078e5 | -2.05379 | -54.29687 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c1c9a81b-8136-353e-9751-9bd8fa486abf | -4.20685 | -41.76208 | 2026-10-08 16:20:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 89c69ad8-1765-3154-b4ae-5aa98b130239 | -6.14143 | -47.95164 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 799f5e15-4150-3399-9e5b-decbc8050b1a | -7.39942 | -45.63771 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 546e6643-addc-3082-8d77-af07cf356908 | -3.46643 | -45.10717 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e5500681-a142-30ac-9585-f36f0cf459f7 | -2.09001 | -46.58014 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 51237ea8-adb8-300b-a36c-fe7a2f07c63f | -4.80824 | -42.74395 | 2026-10-08 16:20:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 40553506-824a-3048-b98c-459b865fedf4 | -6.22588 | -44.98166 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02aa325d-69ec-382f-b1e9-a5925d24bd72 | -6.97216 | -45.12259 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 444baaa8-49e0-303c-8fec-8642fd8ed8fc | -2.45059 | -46.02168 | 2026-10-08 16:20:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3fda2cc6-fa25-3075-8d06-dcb633477641 | -2.98283 | -54.08371 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 65a9185c-b3c2-38e6-9479-ae9f8af3467c | -3.20897 | -50.55103 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d31eaa0b-39c5-3a3e-9081-f149605b116a | -5.96077 | -51.79364 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 75172978-c7c0-3afe-adae-d1aa263bf88d | -8.01154 | -50.15124 | 2026-10-08 16:20:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a883c5d5-c320-3683-a414-9708532023d6 | -4.19299 | -40.40012 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 69df8244-e44a-3a5c-8200-0bc644840031 | -4.83933 | -40.4055 | 2026-10-08 16:20:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5e1015b-1a4f-34ba-a9a9-cc452b1733c9 | -5.69628 | -53.4521 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0309d4d3-ea3e-3ee2-8851-7dfa6590d125 | -3.29411 | -42.68423 | 2026-10-08 16:20:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 909538dc-b2b6-3515-b13f-829c035c747a | -5.51822 | -45.62406 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 272d7bc5-d3c8-34e2-8bb3-b292d164be57 | -7.39026 | -46.20753 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 718eb151-15f8-393f-89dc-80f5c83c469a | -3.89677 | -42.1168 | 2026-10-08 16:20:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 8d9a4268-86f7-364d-bba4-00ac65805734 | -7.00152 | -43.43707 | 2026-10-08 16:20:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d39c9843-758a-34e7-9e2e-6541994c1a76 | -3.18163 | -50.5546 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7acd0f71-b3f3-358a-baeb-ec9f2eff249e | -3.26133 | -41.85195 | 2026-10-08 16:20:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 74959a6a-60c6-3196-842d-24bf16339e1a | -3.97159 | -51.86359 | 2026-10-08 16:20:00 | NPP-375 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 64f6898d-c2a5-3ae1-9f5e-110141091f35 | -6.97442 | -43.29307 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 0c50ea17-606d-39c4-ab64-c37df834ff95 | -5.4336 | -42.64338 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| da5b12d2-fb0f-3c6e-ad1b-b5651d807143 | -3.39963 | -41.52108 | 2026-10-08 16:20:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| be8daab9-0d9b-316c-967b-aef1aaa5b208 | -5.2444 | -38.5465 | 2026-10-08 16:20:00 | NPP-375 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 6af13c4e-91e4-3130-a188-76b99cdd4e1c | -5.75348 | -42.06186 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 39c70102-8797-3bf6-99cd-67a8184c31ad | -4.30647 | -38.10253 | 2026-10-08 16:20:00 | NPP-375 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 08f23ebe-7b4c-372b-9701-8854c623f1d5 | -1.02495 | -49.22218 | 2026-10-08 16:20:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16546758-4ea5-3af7-a8fb-35d20f41a5ed | -2.74015 | -54.12532 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0dd6bada-3826-319a-a5b6-f78943488ca9 | -5.69647 | -53.45982 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| bd136ded-8e63-3efd-ad4c-ec3ea25f80b8 | -6.26647 | -52.88825 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a0ffdabd-f487-3937-9ca6-4a9500298268 | -6.05323 | -45.09454 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 32a81789-0751-3fbf-a076-a58867c86cfc | -3.1761 | -50.59834 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 26e39f9c-9534-3a20-b40a-99943b05d058 | -5.74465 | -42.07526 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| d15d670e-7079-388a-820a-528cb4dddebb | -3.85628 | -44.12793 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 67949488-a342-3f64-a4c3-2ccc62076a09 | 0.38874 | -51.16418 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f5254772-6e6a-311a-a415-2a117b2a83dd | -0.38117 | -49.94191 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b02246f4-e0e6-3ab5-bac6-139928c8466f | -0.20924 | -49.78931 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab470ea4-05e6-3e97-b820-26f5b4c45f84 | 3.51182 | -51.25875 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b7b0723-45e9-39a7-8f05-b40e0d8cbeca | -0.37628 | -49.94611 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08fb1f82-2a82-370c-bf42-2c5776ccede5 | 0.38229 | -51.16737 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 23a194aa-ff17-35bb-8456-356456f5c946 | 0.38357 | -51.15929 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 5584866e-cce8-3d94-9897-58d4499fdc7a | 1.02839 | -50.08746 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d69de638-4a1c-3842-9bf5-d8ef6ad3c771 | 3.54758 | -51.28334 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e78a5219-d2f1-38c8-9537-506662233464 | -0.75156 | -49.3953 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 21a88d55-c610-32b3-b922-d1cfe0b7682e | 3.4936 | -51.46578 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 375e0216-fa80-3931-9c2f-b66bc3975c26 | 2.09356 | -50.84019 | 2026-10-08 16:22:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f86c25c-e419-30cb-a15d-504031703400 | 3.71844 | -51.50561 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c144aaa-d8af-3969-90fe-dafe29c43f83 | 3.49115 | -51.46489 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 583feccd-f72b-31aa-8644-e789c3c01085 | 1.14727 | -52.70514 | 2026-10-08 16:22:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3755b222-8299-3c6d-80d6-bfea0c0e7483 | 0.52976 | -50.80243 | 2026-10-08 16:22:00 | NPP-375 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2012562-7665-34c9-a443-fce23e83947a | 3.51963 | -51.25548 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a830a27-4b69-3070-8f95-f09e3db77aa7 | 3.44444 | -51.71883 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6c99be54-b209-354c-9222-c31d6a93ecbc | 3.54696 | -51.28701 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d2a69fe-d020-3a36-bfc1-cbf8d24cc4d9 | -0.086 | -49.48704 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d15ca1c-abc1-3906-a2dd-641affeae63c | -1.11871 | -52.26108 | 2026-10-08 16:22:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2c0811db-9cd3-3b7d-9f5a-deb712a419bb | 3.518 | -51.25598 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dcc783d2-1a0d-3afe-917a-54985ff5068a | -0.58364 | -49.41533 | 2026-10-08 16:22:00 | NPP-375 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c096b19c-946d-3c1f-8465-8689692579dd | -0.09595 | -49.48225 | 2026-10-08 16:22:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bcf8810a-e4b1-3b44-9cc0-761172644106 | 2.45302 | -50.81706 | 2026-10-08 16:22:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0bfacc01-d7fc-31b8-bbec-4a02207ecaf8 | 3.738 | -51.63023 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a2c12323-cad7-3125-9a5b-c279eb42aa1b | -0.79648 | -49.51012 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0866fea9-2529-356f-a282-9039e8d41f67 | 2.45792 | -50.82148 | 2026-10-08 16:22:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa61ece2-1026-3970-b851-3d5c543a4f12 | 3.52355 | -51.25688 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a9fa604-8f6b-3014-8178-cc31bf6f8f03 | -1.40848 | -52.72383 | 2026-10-08 16:22:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6acf32df-2137-3843-91a2-f9b57fb8289f | -0.79003 | -49.7132 | 2026-10-08 16:22:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1aa9db80-3317-3023-9a6f-41ded65b672d | 3.46614 | -51.47633 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3b2174a5-ebae-3d86-8bc6-98fa0b895572 | 3.75702 | -51.58601 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14fb431f-21d8-3ccd-88b1-428558ac9346 | 3.51245 | -51.25509 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fdb7e94-7024-3824-b829-d7a4f4eb22b6 | 0.03977 | -51.1996 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 680a81f1-9229-3892-8208-0ec78e10e55f | -0.88228 | -49.30607 | 2026-10-08 16:22:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57079d43-18e5-3f6f-9d63-7eb434338cb2 | 2.45243 | -50.82061 | 2026-10-08 16:22:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| daac4b4d-ee5c-3d2e-8ff3-94338f9f79b4 | 3.51408 | -51.25457 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ec9822a-6366-3a91-84fd-325a0a59b7b9 | 0.53963 | -50.77679 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 74d5d68e-9440-3030-a7e2-fb745d91d268 | 0.52836 | -50.77499 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0261256e-ba52-39af-ae34-ba04a2cc6ef4 | 3.78689 | -51.59855 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 022cbd90-dc73-3edb-816c-42abd5d1447a | 0.39064 | -51.15209 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2936ec4e-7b9b-3db0-93de-4add63dda70f | 3.48797 | -51.46485 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b3cb034-b343-39d3-810a-25c45cdbd5d9 | 2.11311 | -50.82483 | 2026-10-08 16:22:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 97b3c181-6db8-31f2-bc84-bf2834a315d7 | 0.53459 | -50.77213 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9316b69-001e-3780-8e83-c4b2468f8f07 | 1.08995 | -50.18271 | 2026-10-08 16:22:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 807c8833-c931-3eab-bdc3-564886efc6d6 | 2.09473 | -50.83936 | 2026-10-08 16:22:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bba2090-4296-391c-bc3a-5b2142a4d324 | 3.51348 | -51.25823 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33b24eb5-01d1-3d25-88a6-ac46429f53b3 | 3.74624 | -51.61577 | 2026-10-08 16:22:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 51380a60-bc0e-3c17-b44f-56e9d809dfad | 0.39001 | -51.15612 | 2026-10-08 16:22:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README304.md)
