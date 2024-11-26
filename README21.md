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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78de85ef-ed21-3041-ac13-3171c78f3789 | 1.94764 | -60.85523 | 2024-11-26 04:36:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5f1a478-4a0c-316a-bc7e-299d8dc3f1d3 | -1.19242 | -46.20092 | 2024-11-26 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c7ebfcd-9e5a-39b6-b90b-750cc351bf8c | -1.93063 | -45.75205 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 904411bd-fcba-389f-a586-9ef34de22295 | 1.25126 | -50.93795 | 2024-11-26 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7facf69d-d19f-3cbd-91bf-f088abd199bc | -1.18788 | -47.66632 | 2024-11-26 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30d81299-2d9d-3091-981c-f8f30f360bb3 | -0.30939 | -51.75745 | 2024-11-26 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3eea0cf-9176-3761-98e0-c70e3e74e399 | -1.4323 | -47.31627 | 2024-11-26 04:36:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8538bb09-2d99-36b2-9476-45af7f078d8b | -1.86688 | -44.76597 | 2024-11-26 04:36:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1729bd19-2e1c-3c95-9e54-c8d64e1a9689 | 2.09798 | -50.96519 | 2024-11-26 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a59b2fe-5a7e-3045-907c-a1aeab265b09 | -1.93001 | -45.75597 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b44830c2-775b-3e59-b429-ab30eedbc662 | 2.68345 | -60.43099 | 2024-11-26 04:36:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 951002f9-fd77-3f5f-a1c9-3befc09a58e6 | 1.832 | -55.9762 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ac3e5fb-e49c-30bb-875a-8fb30fd0edfb | 0.97546 | -50.1265 | 2024-11-26 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55bdbf3c-d5b2-38fc-bdcd-eb885eb8f8ae | -0.31314 | -51.75805 | 2024-11-26 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9717630-4418-374c-98b3-ebeee53c5507 | -1.30467 | -51.7342 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f79d0ca-5831-3ba3-8ccf-2413612d8492 | -1.93022 | -45.75501 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ead2b17c-4535-386d-963a-f84aad32dcf3 | -1.31203 | -51.74669 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b414e7-c229-3752-b694-4d769c32b2a9 | 4.23228 | -60.07397 | 2024-11-26 04:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a74253e-6d39-3bde-91cb-acba022eade0 | 1.83154 | -55.97311 | 2024-11-26 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ea3314f-2824-31d4-8879-e2d0f8a252b2 | -1.70315 | -47.72532 | 2024-11-26 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5428f5a7-a82b-3775-9dce-076b90e0a6d4 | -2.49472 | -45.03542 | 2024-11-26 04:36:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33161fcc-c24a-3f16-ab10-026dcdaef5a7 | -1.70592 | -46.24337 | 2024-11-26 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd49895e-484c-3a25-bd37-17803a8bbc76 | -0.88396 | -51.71774 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6f5cf26-b855-3cd6-8e49-db7d4451dfa6 | 0.67813 | -50.80185 | 2024-11-26 04:36:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8269c4b-d210-3bde-9eba-b66ecaa8c55c | -0.73622 | -48.53193 | 2024-11-26 04:36:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7dbca6a-3de2-3a4c-bb7e-c53fdc27a9a8 | -1.04189 | -51.74075 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 381ebfad-a5a8-3b0f-b89e-58a0719ce3dc | -1.31873 | -51.75217 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15960a4e-f2a0-3f31-88f0-a3048e54e586 | -1.27817 | -52.17233 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4174a50b-ff0f-32ba-811d-882ebd2d1818 | -1.62787 | -47.23117 | 2024-11-26 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 854e0aa9-c65f-30e9-9969-da1f45579a05 | 0.09709 | -49.84294 | 2024-11-26 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2618bed5-d6be-327d-abeb-1a8d36e31d3a | -1.06258 | -52.41653 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7953bb3-fafa-34f1-a741-e44c67ef5271 | -1.31306 | -51.75335 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ce86b95-ecd5-3864-b89a-113d91d99cbf | -0.98532 | -51.71387 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf580cdf-926f-3a3d-bff8-fee401b7b484 | 0.48563 | -50.95245 | 2024-11-26 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f7e5ae-cb80-3b9b-ab5c-65f5158ee87b | -1.82751 | -45.58381 | 2024-11-26 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4893d54f-16b1-308f-acd0-1376762f7eee | -0.09442 | -51.75042 | 2024-11-26 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48a57e79-f300-3840-a712-f87d3e4e9a7d | -1.56325 | -45.68188 | 2024-11-26 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae5aec60-4365-3257-bec2-fd3be79b0b52 | 3.82655 | -59.59837 | 2024-11-26 04:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a95f921c-d87b-32d4-a9f9-54be936882a9 | -1.6098 | -46.05181 | 2024-11-26 04:36:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bebd491-6afe-32a2-9af8-d1f2ef61ca62 | -0.24533 | -48.57973 | 2024-11-26 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8692f38d-724f-3488-b5c8-d614a67155d8 | -1.61574 | -50.18719 | 2024-11-26 04:36:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17da3320-61d3-330b-b0fd-d2464ec9a1e9 | 2.6825 | -60.4246 | 2024-11-26 04:36:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf7de416-173c-3517-84ae-84cf0f896644 | -1.60166 | -47.46391 | 2024-11-26 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c17efdf-dea2-3402-8e98-b1b8f0da4186 | -1.19301 | -46.19721 | 2024-11-26 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 541bedbd-78e8-37cf-91c7-41943856fc26 | -2.32364 | -46.12563 | 2024-11-26 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a471f1-c83e-3332-a37d-bbd68dfda182 | -0.8824 | -51.71964 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cba74eb9-e7d8-3273-9617-1f5f226e3c5a | -0.98698 | -51.71596 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b39b2740-7606-36d8-8b35-03edd2e59a5a | -1.06004 | -48.02454 | 2024-11-26 04:36:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6936539a-b098-36a7-8b30-2c734c455cad | -1.60099 | -46.91144 | 2024-11-26 04:36:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c1f2422-cda9-324f-b39f-0bc755bab6ce | -1.59939 | -46.05019 | 2024-11-26 04:36:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc17cafc-62c5-3242-8d29-b801eafc852f | -1.6022 | -47.46042 | 2024-11-26 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87a5ffda-45b9-37d5-af36-6f5671445b9e | -1.82805 | -46.28827 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f2e9794-dade-369f-8ba0-b0ebb15cf158 | -1.37264 | -52.33234 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bab961a0-ee75-3c4c-a9ff-e567e5555f92 | -1.31139 | -51.73972 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f059876-fc2c-3699-9e65-0ee328b80fa0 | -1.37026 | -52.12835 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01fd21f8-452c-3f11-88bc-ee1540fa0940 | -1.13262 | -54.17773 | 2024-11-26 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f48b93ee-7e9d-38ef-97f3-286dac1969db | -1.30974 | -51.7374 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9750e88-2a90-3cb1-866b-8635c0fd6860 | -1.82519 | -46.284 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b99063d-ce5e-3203-b85c-8c52e1e14078 | -1.29425 | -51.7281 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7964b433-71a4-3ac0-a213-712e054afb3e | 0.67748 | -50.79774 | 2024-11-26 04:36:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 988f8ace-a5a6-30d2-b835-5625fc93ea5b | -1.93375 | -45.75556 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b800e81-a192-35cd-a8aa-45acef421149 | -0.98832 | -51.71885 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f463d2f-5035-3d98-8e0a-c5060adb1d9e | -1.59012 | -45.46304 | 2024-11-26 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b94a87-f0ab-3793-affa-dc0f3905d74d | -1.29055 | -51.72752 | 2024-11-26 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d5898e-cc67-3ced-8189-e74d2967b26c | 0.97196 | -50.12705 | 2024-11-26 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29f8cb1-3d14-39fc-9d7f-818ddc10a702 | 3.82072 | -59.6052 | 2024-11-26 04:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 971f546f-55a3-35be-85f7-4a61c7089f5b | -1.13134 | -54.17915 | 2024-11-26 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e7ca671-a7a7-3cc1-a773-c048ff131846 | -2.09384 | -46.55235 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 461d5efc-957e-3495-8e4f-26f58444fe0f | -0.94682 | -47.09338 | 2024-11-26 04:36:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c33842e-3ed5-3d39-9d0c-deef174fedd4 | -1.82688 | -45.58778 | 2024-11-26 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b288c5f4-a68d-3850-ae2e-5dd39295eb43 | -2.18829 | -45.97281 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c2b0f2-3c6c-3952-92c7-edd6a5ec1c1f | 1.99792 | -50.80449 | 2024-11-26 04:36:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e16be322-2313-3314-86c5-ae8c3f787dc0 | -1.72039 | -46.21877 | 2024-11-26 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41259650-b6d0-39d0-a659-96fbd9b81183 | 3.81987 | -59.59937 | 2024-11-26 04:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9957542-5425-3db4-9f9d-91e125cc4d4e | -1.86858 | -44.76875 | 2024-11-26 04:36:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2ac349c-3459-3a20-a827-bc27ac216f83 | -1.27438 | -52.17172 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb83fec4-850a-3685-a382-384d7efb8dad | -0.88612 | -51.72023 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17dcd9d1-4814-38b1-96b0-b3e7c45b7405 | -2.09519 | -45.96651 | 2024-11-26 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7221310-e2e7-3b28-988d-5251809fd2f9 | -0.87582 | -51.72099 | 2024-11-26 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45f16ad7-f6a8-3044-bb16-a56d1c400dae | -1.56738 | -45.67851 | 2024-11-26 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdfce9bd-1fa2-3103-b9df-e5d652ba133f | -1.39699 | -52.55711 | 2024-11-26 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ee47fcc-831d-3f25-9683-75861031fe4c | -2.09042 | -46.55182 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3f97a3a-ab25-3a6e-be38-24459f446410 | 0.66602 | -50.79531 | 2024-11-26 04:36:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e38bad-e037-3ba6-97de-b476cbce51ab | 0.66242 | -50.79586 | 2024-11-26 04:36:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51522476-d146-337e-97cd-b39b0040126f | -1.81575 | -46.61104 | 2024-11-26 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d27096f-d705-39d8-a2b7-9bc843274dce | -0.75593 | -47.26829 | 2024-11-26 04:36:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f706d8e-5c21-36da-af0d-795d84f028c8 | 2.68313 | -60.43084 | 2024-11-26 04:36:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75b045aa-faa5-384e-be76-8b91a4e958c5 | -4.2382 | -48.70911 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b369705-805c-3806-a3d4-809c09b1c4b3 | -4.04247 | -48.31674 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 930f3284-df38-3fd5-9524-9414f59b1b67 | -2.27025 | -51.91391 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 890c0207-7cda-3f45-9c95-2141a839873d | -3.32147 | -50.31033 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd17f04c-29b9-31c8-917e-2c12be523615 | -5.12342 | -47.74212 | 2024-11-26 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2005c7b-725a-3067-9f74-9ebf3ecca066 | -2.79708 | -45.27299 | 2024-11-26 04:38:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22c6ed87-446c-360d-92d3-fa46842d190e | -4.54133 | -43.29184 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fd60bb26-3c80-3102-9331-41bca947e8a5 | -3.84748 | -47.05658 | 2024-11-26 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8711589-7e0d-35ea-b2d1-683b51bdf647 | -2.94812 | -53.72003 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de4599e-3860-32f6-9da5-1ca5bd0bb0b3 | -2.81154 | -54.02435 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804796b4-1f67-3c89-8703-c1953e16a33c | -3.26178 | -53.27615 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc9d5e19-61fc-3fc8-b6b5-dd14bf585dd5 | -4.29484 | -48.19616 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c28893f2-305b-397b-87b1-4b268aaae265 | -2.72395 | -48.89256 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
