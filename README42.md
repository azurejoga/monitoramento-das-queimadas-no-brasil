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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ddf695d-d500-32df-869e-669e5d2bea10 | -5.22342 | -45.43095 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecf13b4b-9460-37b1-bc00-c80a2dd11272 | -8.58214 | -45.5838 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02d144c8-8a32-3245-805b-69066057a7cb | -8.48982 | -47.31388 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc594659-3435-33b5-9016-b9bdcae42e3d | -7.32028 | -49.61474 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ff9f783-0d3c-3e9c-976d-e6a9ab3f5f0b | -4.58326 | -45.615 | 2025-09-11 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84125d18-fcec-369a-b9f9-6ba1a1de09f8 | -4.92713 | -55.7778 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06bef39b-3e7a-3152-92a1-1dc57f40317b | -5.72315 | -53.59809 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb30e33f-05d0-3167-818c-341f6bbbca73 | -7.78391 | -50.77668 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce8aea75-f8a8-3da6-8c90-56476f74db6c | -8.66336 | -45.73416 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1795aa1f-b2f6-3a2c-82a7-45ab56711f80 | -6.33455 | -44.63596 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f8dc871-f9c7-34fa-8587-017ecc4c8a6d | -6.4051 | -53.65284 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ceb92e2-087f-3590-a470-bc0a301f5ae1 | -6.67509 | -44.12316 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36b443f2-1f64-3607-ac06-db0a9454bbcb | -6.42051 | -44.49726 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1161c31-ee92-3cd6-9d7a-0f9632b3293b | -6.25383 | -43.48723 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea870808-80e4-3516-98be-c7db5af86018 | -7.20159 | -44.94246 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 592dace4-86f3-35ab-8025-c2e79f82cd15 | -5.72925 | -49.21618 | 2025-09-11 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26e1e456-dbd0-32a9-94f5-8109ed31c7be | -6.48044 | -43.62025 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9f50e18-d130-379a-bd22-0ab30935d49a | -7.49508 | -48.26069 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 457eaea6-31ea-36d1-98c2-cbc1cdad6614 | -5.39633 | -42.64612 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fe81f59b-e0ba-38fb-9bab-7225e197274c | -7.73175 | -50.75533 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f076e60-1a76-3500-b14a-9f7ec38f4341 | -5.85343 | -45.12713 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af894a9d-1b16-3d33-8eb1-ff75c8e92240 | -8.53385 | -45.56536 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2335ff4f-14cc-3e70-a96c-0d88bbaf01c6 | -6.28734 | -44.93451 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dd5c626-e544-384d-85f2-0d7beead4352 | -7.38941 | -50.89447 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 188dfc53-ed99-3357-8ce7-a81f921ca8b2 | -7.50309 | -48.25767 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3ce61a0-7684-3017-98dd-b0b4d9df2c50 | -7.84586 | -45.40567 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d8e3ff-8943-3bf5-927d-c934d1162a90 | -5.59767 | -48.11367 | 2025-09-11 04:21:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b399651f-9473-3e07-b762-e55bbb8fc6c1 | -7.71503 | -44.79877 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a2c5a4-aff0-36d5-9d6f-31e862b90ef6 | -6.31772 | -43.40937 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ab46eed-0912-35b5-a4d2-09345bfd3f6b | -5.78907 | -45.45184 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a74bd3b1-ef97-3a35-9d45-c8b4065e3d1f | -5.94214 | -42.79275 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20d3d656-6fb0-3863-bf73-e1623fa9749c | -6.82428 | -45.59483 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a759fc8-ddbb-37bc-ae73-bee5d126195e | -6.41441 | -44.49275 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83445bfc-1ac9-32aa-97bd-80b32d564ecd | -7.5841 | -47.75792 | 2025-09-11 04:21:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 158a1074-d51f-316a-b213-547ae2c76b25 | -6.28909 | -42.20217 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3a592ea-c7fd-3d05-8abf-5150c533a075 | -6.31866 | -47.74369 | 2025-09-11 04:21:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3a625c9-5576-3481-92a9-878952717578 | -8.64113 | -45.72338 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebd82d88-e618-3111-9a78-e651b4af9b5f | -5.41378 | -45.92362 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 968d2922-b5db-3901-9125-4aa7bff82277 | -5.65427 | -43.90342 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdb31dc0-1221-3c7d-b7a7-94a663bd7b10 | -6.67399 | -44.13021 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 913edd30-d6db-3c60-9c67-122522db31e7 | -5.48454 | -44.11946 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e26ea0-4faf-3c7a-9e59-c488ff421503 | -7.35206 | -46.1609 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20591fae-8b98-3ad9-b73e-26d129aababc | -9.15631 | -45.56491 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3419496b-46a7-306b-8e1b-885db8b9991a | -6.2984 | -42.21159 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b874a0f-4f37-3c41-a788-d92ef19aa305 | -4.13523 | -38.70403 | 2025-09-11 04:21:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f47e24f-37d5-3ebd-abbc-992a08660b91 | -8.42544 | -47.27203 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b76f87ef-b2df-3581-b505-f57baa0e8d06 | -6.32228 | -47.7443 | 2025-09-11 04:21:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09acc064-046d-3cae-8f6d-ed38bda247b1 | -3.2163 | -48.61282 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6f29fac-9131-3bb2-afde-0c07deb28a73 | -9.00956 | -46.08647 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce247224-d28e-37ef-baf8-2ec4cc257dd3 | -2.79092 | -48.60678 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2727e63-2f42-35f7-97cf-39bf360da74a | -8.44402 | -47.26731 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a0489c3d-5355-366f-8e8f-eb7751c76aaf | -7.07823 | -43.87725 | 2025-09-11 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f3f1d29-f8dc-3a9c-bb7e-bfcd14b7477d | -7.51383 | -48.27981 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e4a1aa8-9243-3574-b9f6-a3222e8493ad | -5.25317 | -43.76571 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6a6f41d-1ac5-3dc9-9a3c-71d1cccf960c | -5.54806 | -45.08625 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1dfede8-cb4c-3a9b-8829-f6a02ab4adc9 | -5.85949 | -47.05243 | 2025-09-11 04:21:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23459889-1de0-3e69-b994-1c59c4f3154e | -2.78693 | -48.60615 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6384a8e0-8758-35ed-9e80-551a1a5c86c9 | -7.705 | -44.75434 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 149ae78d-4e98-3fba-a2a7-976a35f4b5e7 | -6.25818 | -43.41482 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c153855-ced0-3ed2-95ec-59b9fe417a39 | -6.10464 | -45.93144 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd8183c8-3c01-312f-80f9-6cf1f92ce180 | -5.80967 | -45.68023 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deca823e-71b0-372a-ab91-f477b47c4632 | -3.53989 | -49.32501 | 2025-09-11 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29e50fa8-a7d9-3795-a24a-3362d7756c8d | -6.17395 | -42.67134 | 2025-09-11 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9e3df716-eab2-317a-8cc5-fe8e608f7789 | -7.79014 | -50.76589 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d2de5202-ca3a-3ad7-992f-97ff5e5672af | -8.02557 | -44.49725 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f03c77c-5f67-3713-83d0-dccb15865b2a | -6.38789 | -44.42739 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c0a16eb-c566-3467-be72-700363413715 | -7.08254 | -44.13409 | 2025-09-11 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 473dfd71-4307-3041-90f5-c350d42fc6f9 | -9.00622 | -46.0859 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c7a1f57-54ec-3f28-9aa5-9b18ef20baa0 | -8.9334 | -46.15416 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12ccae88-2e77-37a2-a41f-7f8ed9de5c5e | -5.7542 | -43.73613 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83205f2e-43e5-3aec-b4de-aeea6e01394d | -7.26528 | -44.90622 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5270a96-a1c9-3a7a-a07e-e699b3ff03c6 | -6.8333 | -47.90305 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04e57167-36c8-3487-af18-de07e0a2f337 | -5.35879 | -43.4079 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 121a5c49-2e3b-3d03-a2c3-6ddf89d2dcbd | -6.85694 | -47.8725 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d713275e-f336-3b84-83b7-ff7954c5f74a | -7.48439 | -45.29062 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c306051c-a5b0-3f5f-ba1e-1a5338db5d6c | -7.55884 | -48.21269 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57c8f228-245a-37a1-a98a-221edef2ec24 | -5.67895 | -45.46324 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 092cde6a-e614-3878-9e57-0a056d06c9c6 | -4.27928 | -44.38707 | 2025-09-11 04:21:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 728159ed-0f41-3a9b-b0d1-76ecabc5745b | -5.47419 | -43.42924 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbe6596a-2caa-379f-8244-6935db502671 | -7.58645 | -47.7571 | 2025-09-11 04:21:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c38db0b-1e53-3ad5-a795-5063e93cb7fa | -6.38402 | -44.43033 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85a440df-7d0a-3373-a7a6-5b5ddce4f4a9 | -8.01803 | -49.02687 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c25aff46-8974-3111-bdcc-a4fbcc89b405 | -5.93502 | -45.68121 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4373bdb4-33ee-316c-85e7-c1e70366c3e5 | -6.73228 | -43.39204 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c39d11f0-9945-33e2-9012-76da6dc259e3 | -4.72456 | -43.53285 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d54a5a4-afc0-36cf-a0a8-3bf5f873cdde | -5.68403 | -43.32783 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69f091cd-2fa2-38d9-ab0e-f1e4c8c965e0 | -8.42398 | -47.27286 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10cf7e6e-4484-3499-a5fb-416a6a233f9c | -7.18664 | -44.95079 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faf01366-5153-3a68-86a5-e6068117ebf3 | -3.4192 | -47.60831 | 2025-09-11 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f4f36f6c-493d-3f12-b2db-5c21bec2258f | -5.73227 | -45.29124 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d529eeda-3535-3881-b7ea-6b8cc849b672 | -8.97111 | -46.06932 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763ae3a9-32a7-3a6d-8c9d-73cfc696fd79 | -6.39957 | -43.51329 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2aa86dec-bd79-3939-acb6-4e34259445fa | -7.08396 | -45.34476 | 2025-09-11 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8de36ed-22f0-3888-88ac-2c2640e8d690 | -5.57733 | -45.62515 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a2333d0-a319-358d-a973-5f09af412e49 | -7.38486 | -44.83242 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c27a665-2999-3cfa-af81-b834fda8f38e | -5.57815 | -43.56508 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bec69092-e66d-38d0-8b70-ce3b59f9bf0f | -7.21851 | -45.30939 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 988b4b89-a5a0-3623-9b67-2d67a8c52629 | -8.48311 | -47.28949 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2fa3239-9a3b-37f8-b36d-230a86ed34e6 | -5.27918 | -44.20053 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecf7ae02-f802-3011-b1ec-59d5f6735090 | -6.55673 | -44.78903 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README43.md)
