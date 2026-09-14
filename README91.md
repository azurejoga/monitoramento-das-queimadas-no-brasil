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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ade0fc0-4268-3581-b1cd-5764da0380a1 | -5.81713 | -42.7432 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f73cd3f4-2ddb-3e39-9c69-342a660af8b4 | -4.72239 | -42.28545 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b0ceaa8b-ccc3-3c32-a648-09123507d7c3 | -6.29943 | -41.69465 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ac87fbee-30d1-3f38-8c60-a5594c1069a3 | -8.82283 | -45.8793 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6cffa9f5-d57b-3435-8488-12720476d033 | -7.73912 | -44.71975 | 2026-09-14 15:48:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6148e7dc-38b4-3e66-a11f-c49d27e34c73 | -3.77898 | -40.77036 | 2026-09-14 15:48:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8839d6ee-726a-3098-aa2c-4ae2623b1deb | -5.98446 | -42.56934 | 2026-09-14 15:48:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| c4d9026d-6a50-30bf-9518-fd9ee1e16665 | -6.31357 | -45.04511 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 10659452-d720-3d8e-962a-e44b2ca51054 | -7.11202 | -42.09911 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b270bbc2-10f3-37a6-8ffa-59091b6aa425 | -9.32295 | -44.3515 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd20345e-d642-3558-946b-c92e500c3091 | -6.5668 | -45.32132 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 328c232a-7b73-34e9-93c6-8bf049610390 | -7.47724 | -42.11353 | 2026-09-14 15:48:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2b81793c-867b-336c-ac4f-d4262687d77d | -6.80092 | -43.18091 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8de2a2e6-0645-3353-8f51-da6a2a95fe78 | -3.66633 | -40.5704 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 30d95edf-b230-31eb-ae40-ca138756a68c | -4.08865 | -38.25181 | 2026-09-14 15:48:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5bf15aae-f832-3559-b3c5-c4cc717ec639 | -7.09421 | -43.94991 | 2026-09-14 15:48:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f6975d2-abb3-3236-b26d-a4d3ef296c4b | -7.65123 | -36.1071 | 2026-09-14 15:48:00 | NOAA-20 | ALCANTIL | PARAÍBA | Brasil | 2500536 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c7ad4275-4c24-3074-a3fa-1149aa211f49 | -8.62801 | -36.97001 | 2026-09-14 15:48:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ac089eed-0f44-38a0-8fe2-33689c153efc | -5.89673 | -42.68861 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 03a63145-1706-381f-b0a8-03cefa294066 | -6.49976 | -40.09332 | 2026-09-14 15:48:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d8457a5b-7c97-3c25-a70c-32fedc748da7 | -5.56225 | -39.25604 | 2026-09-14 15:48:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| f08e8bfb-1718-3900-b079-c5d4b89c40ac | -4.45402 | -39.35605 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| e110aad4-ebf4-3578-9d66-90132b39ccf5 | -6.09707 | -45.47383 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b0bd6c6d-b6c1-392d-8c8f-efdcebd074e3 | -6.6769 | -45.06573 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d20712aa-7ef5-3311-a74c-c731e4e9ac66 | -5.89958 | -42.68789 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c161ad43-f285-3b14-a04a-7231ae46d0c5 | -5.55572 | -44.11182 | 2026-09-14 15:48:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f5896d45-c02e-3ffc-91e8-9601dfaa0fd7 | -7.17238 | -44.53996 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68e5b0cf-bfd0-31eb-936a-8548b68a3b31 | -9.96751 | -45.77281 | 2026-09-14 15:48:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9dea2f61-3feb-3499-bc90-17320be7d5df | -3.97303 | -44.31718 | 2026-09-14 15:48:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 68a4213f-bd83-3a8e-bf72-369f1836977b | -7.06389 | -41.5456 | 2026-09-14 15:48:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 10845f3c-7f2c-36cf-b734-23f296e66650 | -7.6095 | -36.32795 | 2026-09-14 15:48:00 | NOAA-20 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3fd38b4-cc16-3656-a85d-6511b71acd9f | -9.75429 | -45.86684 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f6856c72-a153-3fc2-9d41-47a870eac93b | -5.92379 | -45.03905 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3e5a555e-ccce-3826-ae2c-0f5af08adfcf | -7.47767 | -42.11677 | 2026-09-14 15:48:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 30855c0d-7833-3a0b-9935-ea3b6949ab01 | -3.77914 | -38.68018 | 2026-09-14 15:48:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dd0ec856-55c9-31ac-b78b-c4be2909b357 | -4.45878 | -39.35925 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 269bd4f0-5089-3eba-b580-344d1dbd9dae | -5.64075 | -40.85264 | 2026-09-14 15:48:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 2590b2ad-0fc4-3cda-9260-1e98fc4df455 | -7.1671 | -42.11169 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 77fb7b87-9eab-343c-91d8-d2a73ec2a961 | -7.16269 | -42.11896 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e8c29dc7-1eef-3901-a8ef-1e1338258ed7 | -4.72711 | -42.28162 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 54df03ed-a196-30ef-89b1-37fc22177adf | -8.10403 | -39.5849 | 2026-09-14 15:48:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 89887877-e1aa-3c0f-8d66-6dca9ef6e6db | -7.46366 | -45.96455 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6efd2078-3144-3b23-91ae-ca74e997ff31 | -9.99596 | -45.89479 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 1e149eda-8b42-3240-9e51-8bca14ca45ca | -7.08503 | -41.81931 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 83f90c8b-f371-317b-bd77-d0a25a69f813 | -5.11604 | -41.07652 | 2026-09-14 15:48:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3c5df600-05ae-397e-94ba-453b4a778012 | -8.06665 | -44.02357 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 88a93537-1c53-349e-a530-543c7fcd2374 | -9.98591 | -45.86938 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 290724ad-fc14-37df-b8a9-9edc6ae23518 | -7.02153 | -44.63143 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2e3c2b5d-40d0-3214-b59b-2a5cf13d36ee | -5.41062 | -42.2293 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 05e39a0f-f452-3f1c-b64b-20c8d82d4c46 | -6.79759 | -43.76058 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 41463401-48be-30d2-a5ab-86669d238809 | -6.33305 | -38.97376 | 2026-09-14 15:48:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| ad09b300-840b-3936-b20b-93ba20b45d76 | -7.10074 | -41.77938 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 647e47ba-5e01-3cf2-97ba-0b0fd150503b | -7.77759 | -46.66464 | 2026-09-14 15:48:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2732d31b-ed6c-3c6c-b188-0cf8811d06ea | -3.4251 | -39.61457 | 2026-09-14 15:48:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| bac1382e-cf93-340f-9c5f-89cfaa0a8d2c | -7.09273 | -42.11515 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d69cdf0a-afd7-3441-a289-2630e215dfde | -8.80295 | -45.88774 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e6776a47-3a81-3e3c-a93c-236e461e086b | -5.86928 | -38.29944 | 2026-09-14 15:48:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 786d40ad-b9ef-349a-b5a9-5063a2ff4b46 | -6.64421 | -41.784 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9eed5628-a179-3031-8d2e-a0771a3eff1a | -5.55633 | -44.11619 | 2026-09-14 15:48:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c65e74d5-999b-33a6-8d89-ff8020bf1738 | -7.45678 | -43.08481 | 2026-09-14 15:48:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0ebe3725-ea7e-3c3d-a39c-8f130c61c26b | -7.02029 | -44.62178 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 87bfc6cc-8f7a-33b3-a180-80140dd322ab | -7.16225 | -42.11564 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| b28f931f-316d-3a0e-9e8b-473ef8bcc893 | -6.38176 | -44.88221 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b0174cf4-4766-3725-8089-567b1722275d | -6.83465 | -43.51374 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 169733c3-f91e-399b-b4e8-b4ac7ac320e3 | -4.3811 | -39.23811 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b5a5f3dd-74f9-3970-93cd-7e4ffa0f3cd4 | -6.80656 | -43.18006 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 845db51c-e6f1-3cbb-b8e7-d92a8d661852 | -8.04396 | -45.5495 | 2026-09-14 15:48:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9f8c3507-a46d-3a16-9196-cec81566dabb | -8.82367 | -45.8861 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4b048770-27f1-36fb-abaf-621e4c080902 | -6.78001 | -35.83437 | 2026-09-14 15:48:00 | NOAA-20 | CASSERENGUE | PARAÍBA | Brasil | 2504157 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2f25e999-69a5-38f7-b5cb-14ba7acaade7 | -3.78885 | -40.77377 | 2026-09-14 15:48:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d7ec7f64-66b5-3bd7-af10-d59c2a15343d | -6.67739 | -41.66385 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3b0c2404-fe0b-36fb-9274-1e0e629082a4 | -8.70589 | -39.60719 | 2026-09-14 15:48:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 045f1745-5e1f-3d89-ae39-0e1b5272cced | -7.19631 | -46.11982 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f67eb700-42c9-3153-95d1-ebc60ba7b01a | -6.67898 | -45.06188 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2c89002-48bf-3d39-aee8-062ca0aca650 | -3.54052 | -39.08828 | 2026-09-14 15:48:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 582bbcb2-2c04-3903-ad24-56c66d29523d | -6.82778 | -43.5065 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3f4ca0d4-3ac6-3659-8767-86a239363611 | -9.14946 | -44.77603 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 66fa8ecf-9539-3236-a5e6-9e55981945a5 | -8.59273 | -44.49144 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 79818cfb-8ce7-36ca-b977-8a86318dd338 | -5.92269 | -45.31042 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe66dbfd-370c-3a20-81f9-f5c3fc0fcbbe | -9.23141 | -44.8025 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 99fcf0ef-658e-3e02-8981-10aedfb5dc5b | -6.43425 | -44.95895 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b937c8b2-f9d4-3453-a95b-dafe7ad5fe32 | -8.57122 | -44.49956 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e7cfc76e-55af-3ff6-8c2a-e5eb0afc540e | -6.65834 | -43.65394 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 2444e65b-090b-3d33-9828-75a3913d3077 | -7.09664 | -42.10456 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 84aabb16-ddf0-3f82-948a-26df9d9976ce | -5.40973 | -42.22312 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a1051dca-c16b-3931-82c2-8747939cb1aa | -8.49446 | -44.5783 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c3522972-ff48-3dd7-a549-4f3e9449f55a | -7.16135 | -42.10905 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 83264ae6-b7c0-3d7f-a497-f813f1822238 | -6.56777 | -43.16274 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ef42793d-830e-3d03-afa4-32e127819a2c | -6.33547 | -43.36324 | 2026-09-14 15:48:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 113f5c02-a2da-3c49-ae39-eac4ab936f06 | -7.34387 | -46.7886 | 2026-09-14 15:48:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 224ed264-916e-3a9e-b1da-e3697411cfce | -3.9289 | -42.99753 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| c8d14d08-9fbe-38cc-a404-7f10ee54d0ca | -6.78818 | -42.88486 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| df39bd25-8b2a-3a96-8019-0716d24bde88 | -3.96193 | -43.11411 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 601433c0-09cd-3de6-9eeb-a3961ecf36cf | -3.66627 | -40.55268 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b8180ead-24ab-37f7-9d27-c20046d59f37 | -4.71635 | -42.28 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a935de6a-22d9-3daa-94ab-1ea3603bd97d | -6.32527 | -44.17609 | 2026-09-14 15:48:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b3ae418a-0290-37aa-8e28-46405d0bc680 | -5.91997 | -45.03233 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c7bcc8e3-15bd-301b-80fd-a104ab4ee470 | -8.12228 | -44.06532 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0776d3fa-5171-3b41-9783-56966c2a249c | -9.99439 | -45.88148 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4d33fa99-f4cb-39c7-93c4-9739bf5a8474 | -5.67892 | -45.03606 | 2026-09-14 15:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README92.md)
