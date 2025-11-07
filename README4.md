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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6af1b09b-2cda-3ea5-9844-869c01ee89b4 | -4.68246 | -45.84691 | 2025-11-07 03:34:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1f524dd-2891-3d32-b154-c0b2ec657265 | -5.86972 | -36.87217 | 2025-11-07 03:34:00 | NOAA-20 | SÃO RAFAEL | RIO GRANDE DO NORTE | Brasil | 2412807 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00cf092b-3f58-3a1c-bb5a-12345029c7d7 | -4.39348 | -46.44076 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 056ae0c7-9251-3e66-af3b-8bf3f8a8a92b | -6.50627 | -35.34116 | 2025-11-07 03:34:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5ee055fe-174f-32f2-911c-2661b6cd1508 | -6.34387 | -35.15046 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3718333a-33ab-3d29-ada4-71ea2eb1756a | -3.77567 | -43.99126 | 2025-11-07 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9546e70-afda-3936-96a5-c6bf1cc3fe7d | -6.34329 | -35.15409 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d3e173ed-40cf-3235-9d28-f7c550ed4d5e | -3.8207 | -45.35071 | 2025-11-07 03:34:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24bc6da7-0960-350f-8e9f-2830e4f4ec2a | -4.70576 | -46.44249 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faf5e4a0-921e-308f-8278-ce32a6b78993 | -5.18581 | -35.61076 | 2025-11-07 03:34:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cbda1ce3-4a5f-3eeb-8548-bb00fdd4686d | -3.77046 | -43.98552 | 2025-11-07 03:34:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33120406-5a62-38b5-be6d-fe3512ee8db5 | -4.46726 | -43.22916 | 2025-11-07 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f10e6100-5f28-3117-8b25-a467d5f4905b | -6.59007 | -35.25306 | 2025-11-07 03:34:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 157cb7ce-b4e6-36a5-9f17-c61f5962a961 | -4.29949 | -45.89128 | 2025-11-07 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f581048c-ec82-32b1-a51b-732dde96d243 | -3.60034 | -43.51652 | 2025-11-07 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc08ba36-efd4-30b6-8bb7-2ced2830592f | -4.98099 | -45.06215 | 2025-11-07 03:34:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4560a589-e3f3-32ce-9155-fe1ceba84c1b | -3.59963 | -43.5206 | 2025-11-07 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5021a993-84ae-3498-8a32-9c64e5b1a4ca | -4.44919 | -46.44628 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2388e92c-0548-34ad-ad19-364b5a4e2451 | -6.34107 | -35.14627 | 2025-11-07 03:34:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a3d7d944-6e31-394a-814b-66ac0381034a | -4.44991 | -46.44427 | 2025-11-07 03:34:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c8b2c7a4-5c6a-3305-95d6-efd8b89e7065 | -5.74899 | -40.79908 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5cc364fc-ae7a-314e-914d-c997f09c5830 | -8.75643 | -44.23556 | 2025-11-07 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4db1d471-4411-38a6-ab79-ff7d5b7da740 | -6.26331 | -43.68113 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb63c9df-ba4e-321f-a472-fce682dfcea4 | -6.26409 | -43.68977 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d77446a5-92bc-3838-abdb-e43933444cdb | -6.21402 | -40.69365 | 2025-11-07 03:36:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 487a9e0c-7fd8-3b9e-a6d1-cda266588b9d | -9.61718 | -36.7649 | 2025-11-07 03:36:00 | NOAA-20 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1ecac4ae-3336-3df1-b675-c8f37736c1e1 | -5.08124 | -44.82274 | 2025-11-07 03:36:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a62e01-a820-3d64-9783-826ff313197f | -10.28157 | -36.35857 | 2025-11-07 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74ae516c-723d-3c10-93d5-05f964a3e074 | -10.05416 | -39.43166 | 2025-11-07 03:36:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 272e9e42-b656-342c-b83a-505e2da858b2 | -6.26836 | -39.56628 | 2025-11-07 03:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5a0ee4f-e90d-3158-81aa-462d3e245c0c | -5.76285 | -40.83218 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a023fc8-10ce-3a1e-8e9a-54fb509d5c87 | -6.97239 | -39.07629 | 2025-11-07 03:36:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59c6050b-51e5-30c7-b4a1-cf86fa51aeec | -9.98342 | -36.05801 | 2025-11-07 03:36:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| f8fbc03e-ae89-3720-9410-3ec1996fde33 | -6.87914 | -42.85506 | 2025-11-07 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cdbc70ad-fbcd-3448-b3b6-62091ed54b7c | -6.64689 | -43.61618 | 2025-11-07 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0fb75b32-6deb-3521-9a75-8560e2504361 | -7.42943 | -39.04208 | 2025-11-07 03:36:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 076a6f38-4df4-3fd2-916b-a50ca4be248a | -7.28358 | -39.38782 | 2025-11-07 03:36:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf3b6c40-e0f6-3f34-b0f1-6dfcd58133a9 | -6.46768 | -39.12935 | 2025-11-07 03:36:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb4389f5-4665-3b53-80c7-44439919eb81 | -5.75375 | -40.79964 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f97d4e46-05a3-32d5-b1fc-ae6fde540f83 | -6.73597 | -39.65366 | 2025-11-07 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce303995-59c4-325b-b300-60a42fc95228 | -11.57496 | -40.0346 | 2025-11-07 03:36:00 | NOAA-20 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87673221-038c-35bb-9101-310dc530a41c | -6.26557 | -43.6816 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fb4f07f9-357f-3f91-b656-3fcaebd7d3dd | -7.07858 | -39.82569 | 2025-11-07 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e84658a-8498-3460-91cc-255167bf0007 | -5.76676 | -40.83788 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1693d994-74e7-3d08-b213-6140ffbff8ed | -5.268 | -47.16116 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7183805-b598-3f16-9502-470f582eadc3 | -5.76322 | -40.80109 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d9c5626-1834-3427-9a6f-bb9471ed5fb6 | -6.87854 | -42.85844 | 2025-11-07 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a5fa15b-290a-3d83-b794-54a46fe248ec | -7.27518 | -39.3866 | 2025-11-07 03:36:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 209ea0c5-ba0e-3c61-adf2-fce207328b1a | -6.45394 | -39.13469 | 2025-11-07 03:36:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7570c9d1-2483-317b-86f5-b3dc10863dce | -5.77319 | -40.8347 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c23cbe89-d61d-3895-abbf-4abbfee61e08 | -9.9862 | -36.06227 | 2025-11-07 03:36:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 71482318-64e0-3bab-bdae-f44bdfd34994 | -7.62773 | -39.73646 | 2025-11-07 03:36:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de3bd3f2-1199-3aec-80bc-856d252e6a96 | -8.31134 | -42.21177 | 2025-11-07 03:36:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e9aeaae2-267c-3d30-ab76-060b6dcd1871 | -6.51235 | -38.73625 | 2025-11-07 03:36:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48b138fd-5ce0-374d-80c9-bad9bba73b29 | -6.70144 | -39.97032 | 2025-11-07 03:36:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8a185b16-a34a-36bc-9afe-21878a0efde2 | -7.14164 | -39.43163 | 2025-11-07 03:36:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4544d6cd-ec31-399a-90f1-69076c9a1a5d | -6.26485 | -43.68559 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21ba13e1-692a-32fd-957d-8b84ea0361c2 | -5.7559 | -40.81572 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c3cf7d09-5fd7-3f51-bb9e-b24f7299e78b | -6.64975 | -38.83845 | 2025-11-07 03:36:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4a9fddb3-9eef-3caf-9748-c505b6638d06 | -5.76414 | -40.79555 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d480559e-fc9f-3aec-90f1-1c7073be189d | -6.64759 | -43.61225 | 2025-11-07 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc97669d-28e5-38f5-8b92-1e7b03e7f635 | -5.76357 | -40.83404 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56e40c19-682d-30b1-a941-2df64cda0082 | -6.64829 | -43.60834 | 2025-11-07 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7728cd73-0aec-3092-8de5-ee679bda1147 | -8.31236 | -42.20601 | 2025-11-07 03:36:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6249c3c2-7e54-3eb4-97b0-7d6e9b486316 | -5.27813 | -47.16747 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97cf72cd-c700-3e05-8914-957f06907f13 | -7.50972 | -38.01659 | 2025-11-07 03:36:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 9470024b-9680-372e-b0fe-ff16cb5c3a6d | -5.75117 | -40.81491 | 2025-11-07 03:36:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e287e83-8411-321c-9601-bc5496c19ea4 | -6.73783 | -39.65757 | 2025-11-07 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa3e8666-7fc3-31d8-bf01-c75b57fb3468 | -5.75849 | -40.80035 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2fe46e2e-6fa2-3977-8d81-9091e89eb00c | -6.71064 | -42.52736 | 2025-11-07 03:36:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99aa081c-3162-3088-a80e-6218b9fa1e29 | -6.26261 | -43.68515 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 878ff8e5-403d-3174-ab07-f4403f3cb57f | -5.76889 | -40.79619 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5129e8f9-81c3-3433-8f37-a831e1399187 | -7.13939 | -40.46238 | 2025-11-07 03:36:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 43aae53b-7a63-366e-bee4-4b487cb30f2a | -7.22476 | -37.24931 | 2025-11-07 03:36:00 | NOAA-20 | TEIXEIRA | PARAÍBA | Brasil | 2516706 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b80216a7-93e7-3c82-bec0-201d64e360d9 | -5.08209 | -44.81783 | 2025-11-07 03:36:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faab4975-5d0b-39b2-9f2b-cc481ee289ea | -6.64967 | -44.49137 | 2025-11-07 03:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5299faa-4ae6-32cc-8b14-e4c80e1d446e | -7.18705 | -39.6726 | 2025-11-07 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 39149a2d-e874-35c0-a4c5-fd8e948435c4 | -5.95126 | -42.17649 | 2025-11-07 03:36:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da2133f6-deae-325a-a632-fcdbcdc694c4 | -5.75463 | -40.79441 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0e0802c-5e4f-3044-8ce6-cf1f9480fdc1 | -5.76809 | -40.80835 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a379c7a3-cd3a-3fe9-8892-a91462e207b7 | -9.98281 | -36.06169 | 2025-11-07 03:36:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 98.0 |
| 81182a51-3953-3f70-b617-1e36317d1ae5 | -5.3669 | -44.73494 | 2025-11-07 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14cbe3c5-d238-3b33-a7a1-dcac89e54e63 | -5.75939 | -40.79499 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3319108-e88f-31b6-9bd7-0840f8676600 | -6.27051 | -43.68666 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23fc197d-9553-3937-a10b-634db3dc525f | -6.73956 | -39.65863 | 2025-11-07 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea1132f4-61e5-3897-87e9-f74c3056bcd1 | -5.76986 | -40.79828 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9a278f5f-9419-3f36-9877-5da5f441d7ae | -6.8443 | -39.44513 | 2025-11-07 03:36:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcde64a6-8145-3f31-857c-71fb0681b000 | -7.2842 | -39.38415 | 2025-11-07 03:36:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86c8ac77-7dd7-3110-9376-785e9b662f22 | -7.14019 | -40.45786 | 2025-11-07 03:36:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 277ead79-9616-3476-af8a-f62947145ce5 | -5.75284 | -40.80503 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8937c031-4843-33de-b156-192be126990d | -5.27693 | -47.17405 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eec452db-1588-3539-ab9b-0aa313c56873 | -6.26189 | -43.68935 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a5b0b25-b85b-378e-9a99-c2ac4ca4b2bb | -5.75759 | -40.80565 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52449271-baf5-350b-b05a-2725e64c5053 | -6.26906 | -39.56215 | 2025-11-07 03:36:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7c8a944-08f5-326b-b3af-c491e03ce031 | -5.26984 | -47.17264 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9694fc87-f909-3aab-8613-46e823955f0e | -9.98681 | -36.05858 | 2025-11-07 03:36:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3a1fe8a-c326-3dbb-9d9d-1a319468c335 | -7.19343 | -39.91907 | 2025-11-07 03:36:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a705709-57ea-3ab3-b90d-fb6305b0bf06 | -5.76236 | -40.8062 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c708f3b-61b2-3707-adfe-924116409080 | -7.38525 | -39.6306 | 2025-11-07 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b2754dd7-3a4d-31a2-a8e4-7e154c72e69d | -7.13823 | -40.4599 | 2025-11-07 03:36:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README5.md)
