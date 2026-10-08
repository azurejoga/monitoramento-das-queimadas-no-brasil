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

## Dados Diários - Página 278

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5efcb838-85ba-3b41-8e32-b0d897f15979 | -9.36604 | -45.94067 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| c15fbc62-4eb7-3191-82af-dad54089dcaa | -12.04266 | -43.43423 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d7de477d-226f-3db7-8042-a1d66f0f7947 | -8.62014 | -44.87897 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 6496a13d-4b4c-376e-b83c-2e7c494f3718 | -8.28405 | -45.729 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 3f15df6c-564e-3b74-9413-265269975476 | -11.74846 | -43.64176 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5aa6002a-4ae9-3272-a486-c5406d685717 | -11.40525 | -47.5713 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a5e455ad-0dae-3489-8de9-5132c949d052 | -13.37598 | -43.88295 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c3c91411-fd96-38a2-a505-6eea901efd58 | -9.45675 | -44.62555 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 68f53481-d885-3f11-b49a-ef462cd70c6b | -12.19281 | -44.64901 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8f54f950-3a45-397b-8464-1e38ceac46e1 | -3.0447 | -57.4851 | 2026-10-08 16:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 05866023-340b-3c9e-8e88-44e8074c9ebf | -2.572 | -56.1646 | 2026-10-08 16:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 176.9 |
| dbca67b7-f01f-3633-8472-a51cd7715048 | -5.7321 | -41.6349 | 2026-10-08 16:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| ccd12bb0-f271-31c8-bf75-ad2e0bc5c71b | -8.9501 | -45.1334 | 2026-10-08 16:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 296.5 |
| be6af428-9abc-356e-9788-f81310d8b5fb | -8.537 | -66.9764 | 2026-10-08 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| dc379957-3f27-374d-a24a-b1fc9af44b91 | -12.1545 | -44.7547 | 2026-10-08 16:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7669f666-ae70-377e-ac22-1bb227676615 | -2.788 | -57.6261 | 2026-10-08 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 61bb5a7f-917e-3942-9e69-c16c168578f6 | -1.4118 | -48.9318 | 2026-10-08 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 44c627da-09db-3f6e-bb18-af52d111a2ae | -12.232 | -44.7194 | 2026-10-08 16:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 6bf57371-61dd-3078-b669-4c76153abe6c | -1.856 | -57.057 | 2026-10-08 16:20:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6b1c6e86-869b-3677-b9ac-451d51ba35b8 | 3.5448 | -51.2772 | 2026-10-08 16:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 00553e1b-fb29-3a8b-92f0-d20190960883 | -4.09508 | -45.90722 | 2026-10-08 16:20:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 228bd437-0d85-3f41-923b-eba78c2e055e | -4.90585 | -37.29733 | 2026-10-08 16:20:00 | NPP-375 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9e7d91f1-16e5-3368-a0ed-d251eef2bc65 | -3.81753 | -44.62042 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ee759ad-58b8-3b2a-a0cd-f981d728e4fb | -5.6217 | -43.0567 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 50cf6941-b9ad-3c20-811a-2f1f461672ea | -7.76785 | -44.17968 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 68651841-482b-3644-9db2-5de33deb4c5a | -5.95973 | -40.92519 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| ef8c6c76-6b2f-3919-b19d-a610a2c89095 | -7.18444 | -52.62927 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 29a25133-19e8-3ea9-a948-a2c53b9b094f | -5.16593 | -45.1762 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dc86d178-b8c5-35a9-83d4-694abf47a6a0 | -5.99335 | -43.61493 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 937ca519-d009-3a8b-82f1-3c934cbaf8c7 | -6.95376 | -44.41626 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8982c798-e8dd-3ddc-8795-afa51f5f1f4a | -5.99404 | -43.61962 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4653cc1f-f4ea-3e95-a35c-1ab8173f9d99 | -3.5509 | -44.56379 | 2026-10-08 16:20:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| c0b98288-6687-308b-9395-56b89508de30 | -4.18938 | -44.4545 | 2026-10-08 16:20:00 | NPP-375 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2c1e46e8-1d64-353a-9da0-d6bbb78ff4eb | -1.41551 | -51.53151 | 2026-10-08 16:20:00 | NPP-375 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99d8b8fa-cbb7-32e5-ab3d-68fbe117e95a | -6.60362 | -37.89931 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 3ba309e5-634a-3b0e-8a12-49b4cb236f51 | -6.20355 | -40.8031 | 2026-10-08 16:20:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 15b589a1-7517-34e4-8c41-ee49b713dff2 | -2.50879 | -48.34954 | 2026-10-08 16:20:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d049e6ad-78aa-3058-a6fd-0b16bf767dc9 | -6.83802 | -39.56673 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 459835e4-2779-33cd-a59e-ced10809ad4f | -8.26742 | -46.91142 | 2026-10-08 16:20:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b7b5fdce-bafe-3f26-8085-a1d8b08cbdab | -6.85801 | -41.74461 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 4edadf4c-77e4-3660-997d-1622b622ba72 | -5.93888 | -44.32548 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f3c0bc2a-d203-359c-91fa-bfb45d990a7f | -5.71188 | -41.75791 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| a27a8162-f106-3b91-9064-5671ac4903d8 | -6.03215 | -42.71517 | 2026-10-08 16:20:00 | NPP-375 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 6649ea23-8f51-32f5-8cad-51164e7c4f17 | -6.15004 | -47.93765 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 520b32cd-4baf-3431-979e-c3faf5844bd8 | -2.74231 | -54.13982 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6b6c1844-bc8e-34c0-b56c-8e086f59e3c5 | -7.19132 | -44.28204 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 94990ca9-03e5-32b8-b393-720069cd80a0 | -7.78291 | -46.74511 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c4ed26f7-7257-356c-b295-f1335a6343ca | -5.98714 | -41.36146 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 4c815c94-45f5-307f-ac84-84aa9dc35fb7 | -5.30889 | -45.72418 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1206e2df-2e67-3263-8411-a66b2f17ce69 | -4.35419 | -43.80099 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f39537b6-8479-33dc-a5bd-bd8eb385448f | -6.20017 | -40.80364 | 2026-10-08 16:20:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e0c43fc9-2524-38b1-976e-4b304693e7e1 | -6.98623 | -45.12893 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 03f5e2ad-8048-3fa6-bb46-467652cc8dc5 | -6.63094 | -44.89831 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 99a709b1-a7d1-3dfd-a14d-136f59941c46 | -7.72067 | -44.73209 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5621ae7b-48eb-3b48-97b4-aa452085ab7e | -1.43056 | -51.54799 | 2026-10-08 16:20:00 | NPP-375 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 42475c51-be79-3d31-9eeb-8d4b31bd0ef3 | -6.03722 | -51.72427 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a12eb68f-860d-303a-a36e-b2749ca5c2fa | -6.24173 | -38.47841 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 99ccbeb3-b23a-32d6-a70c-c75fc3faa189 | -2.98904 | -54.07531 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| fa5e4f24-9b78-3d29-9111-25b7f6fccee5 | -7.85845 | -44.95787 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8938efa-a0e3-3edf-929a-69b5aa9d6807 | -8.53237 | -49.56008 | 2026-10-08 16:20:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 619cd2a6-e209-332d-8c18-87a6988f30f6 | -7.39595 | -44.47275 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1e7e8172-9afa-3495-ab39-97e0347e0a1f | -6.02057 | -42.71247 | 2026-10-08 16:20:00 | NPP-375 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9d95c2cf-ffb5-3310-a6a1-7e52c5ac4d87 | -1.40015 | -48.94392 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c4902ad-30e4-3410-9de1-f04e1b5cc8f0 | -5.98927 | -40.93139 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 104be219-5d06-3232-91f6-66c47d109230 | -8.21876 | -46.37014 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 52f3a85d-a31c-3d79-a03f-dc485d0272cc | -5.51254 | -42.82601 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 74720f13-c40b-3562-844a-c9c9e349d852 | -2.07184 | -46.57765 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b4df7b34-8833-3e8b-ad0c-f09405fcf138 | -7.1028 | -45.31522 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c9cc1ba-8544-34e1-abec-5686d20a854f | -1.87919 | -53.96867 | 2026-10-08 16:20:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4b6d7f90-5773-367b-9cd1-073eb88158ea | -6.75453 | -45.13346 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 67f468e8-cf21-3528-8957-d132142a7521 | -6.97447 | -45.13876 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ed12012a-c7b3-3831-a3ec-5716e99d41b6 | -3.44851 | -45.09881 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a2bc520-c26a-3e81-afd9-c02b1b4a2a47 | -5.77465 | -42.0587 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d9e056ca-2568-32d1-8e9e-ac37c5967166 | -7.04407 | -45.43903 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b6f01916-6009-32e2-92be-8952cd7ccd4e | -5.73937 | -42.06392 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 06f8fa46-310e-3de4-a82c-afda0d88d6eb | -6.93511 | -44.56852 | 2026-10-08 16:20:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b1ccd364-10ae-3c35-9c9a-7e803531f4cf | -6.93042 | -45.26451 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ed76b264-6690-3f2d-9874-f685cf7d6b87 | -6.84832 | -39.54739 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d5c0e89c-79f5-3228-9c57-a8983beb1cf7 | -6.32423 | -37.74667 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c4047de0-d6fc-3bfb-881e-47148d9e53da | -3.81416 | -40.46328 | 2026-10-08 16:20:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 9749a840-84e8-38d8-ad56-6e5fa94289f8 | -5.71617 | -41.64412 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 68fcefe9-d668-3350-a494-a92066d5cab2 | -6.70766 | -44.98714 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 52f55013-2af1-35fa-a554-74bd86780b48 | -6.57246 | -41.61495 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| fe5224ea-f7d4-39a0-9a79-245010ee7299 | -5.91519 | -35.37514 | 2026-10-08 16:20:00 | NPP-375 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2381a963-9c05-3d53-8156-cc75cd996c54 | -5.92981 | -44.28482 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 10dbba4e-b704-351e-a922-d5ee6fc4bcd3 | -5.70093 | -41.73214 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7de59a8a-8c36-37d7-b275-d2ba29a71c7f | -6.60078 | -37.90329 | 2026-10-08 16:20:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 0e0a5ed5-b35c-379b-8ed5-2582b8172975 | -3.81826 | -44.62551 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73f33e50-c512-3fb3-8815-f3a3b452a23c | -3.01426 | -43.34457 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 010ffbf8-a82c-39f2-9bfe-2660d6da2ab8 | -2.08065 | -46.57633 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 279.0 |
| 5ad9156b-e199-392b-b8ab-759e45696207 | -5.38063 | -44.20432 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| cc868050-8f3c-39d9-8215-31b290d9b937 | -6.1292 | -53.05556 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| fc0e9fc4-709b-3243-8040-9b7e26aa54c1 | -5.75139 | -41.64277 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 1586d0d5-5e98-3a29-93cc-432c8fdae90b | -4.05321 | -38.94121 | 2026-10-08 16:20:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 773a6d0e-62f2-35f8-beef-cb3ba08177dc | -7.5588 | -46.69063 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a17a45d9-fbca-365d-95a8-577b852dc8a5 | -7.20161 | -44.29558 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5eb77cc9-3cba-381f-9c42-1e27a0d08c7e | -5.92907 | -44.27965 | 2026-10-08 16:20:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f56548a5-b19b-369c-a95e-896cf82605a7 | -6.31828 | -45.0577 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7c1070db-8608-3b6b-b547-972c7ded49dc | -4.29555 | -48.60561 | 2026-10-08 16:20:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d74c926c-2bb3-369b-98f5-f79015905602 | -5.34504 | -45.72739 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README279.md)
