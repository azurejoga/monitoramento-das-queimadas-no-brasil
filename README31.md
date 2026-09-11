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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 468884c2-7644-3dc8-baeb-b8a81f6304a1 | -1.77331 | -54.94709 | 2026-09-11 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 421fbc67-5cea-38dd-933c-e1866d52ac62 | 2.49649 | -50.98982 | 2026-09-11 05:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4836d711-6b46-3b2d-a4e2-a43333624672 | 1.28487 | -50.67937 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92d77440-addd-3034-9f4e-412177a58ebc | -1.77422 | -54.946 | 2026-09-11 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83d070ec-9341-3b34-bf73-4d977cde0cc7 | 2.51346 | -50.85099 | 2026-09-11 05:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61691457-2069-397e-9693-1afda6d5abb4 | 1.28696 | -50.68835 | 2026-09-11 05:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 05a653df-07a9-35c4-9de0-0129107d0d0d | -3.07645 | -51.33889 | 2026-09-11 05:46:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f8ec07bb-6896-3c6b-b961-0868ac5bec84 | -6.7697 | -59.42962 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b2a31c30-eee7-37d1-8b74-9e28620f7eaf | -5.37223 | -56.02681 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ebab543-ce30-3684-ad24-5ffcf7652f41 | -7.52115 | -64.50828 | 2026-09-11 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faa0973e-e8e5-3668-b3c4-f54e8948a06b | -5.97155 | -57.78486 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1896d1-1816-3dac-897a-da73e4dddaf3 | -5.97606 | -57.78194 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c004ddd-f9df-3b74-8578-e5b32b28f0fd | -6.20624 | -55.27774 | 2026-09-11 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5da1d3aa-39a3-3b4b-aab9-ed4f545dbfd3 | -5.9771 | -57.78057 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2691999c-72ee-33eb-b830-389b69e3b153 | -5.36928 | -56.02636 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48650c35-71db-3df9-bb5e-15df8f58704b | -7.24207 | -59.52052 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a573be3-9816-36f6-9848-787bfef1d7c5 | -6.2382 | -51.68992 | 2026-09-11 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 889c08f1-6207-34e2-9a2a-0bb36e67224e | -6.79081 | -58.89125 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22dc501-8bb4-3ecb-9b78-f194c1684876 | -6.10956 | -57.6317 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eda4b390-fe41-39a0-9d41-e1f723bc08e6 | -6.79466 | -58.89636 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0682345-bd17-3282-8ba1-5a948a98ec1b | -7.01611 | -59.77835 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a14b2bdf-fa36-356c-8681-12e0abf58a0c | -5.97756 | -57.77124 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f111db-0379-332a-829b-f0e58ee76dc4 | -7.84472 | -56.58403 | 2026-09-11 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8a411f-cea2-3ea7-9860-c851d49d8224 | -5.37273 | -56.0234 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce04ea81-1263-3eb5-a0be-bc00b5e290d7 | -5.37024 | -56.01951 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1479e049-9e40-3615-8fde-f89a3828d7a1 | -5.36784 | -56.01925 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3306d5e1-d11c-36ef-ae4f-b65c14ae851c | -6.1896 | -57.75521 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c43dbd1b-1892-320f-be75-64f019f3fb83 | -6.20052 | -55.2769 | 2026-09-11 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd420321-ff80-3423-9013-ca87388e647f | -5.97789 | -57.77522 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3501431c-ccf2-3c12-bfcc-3929201dd607 | -6.50506 | -58.38358 | 2026-09-11 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 694048bf-7822-3dc5-9941-8875912bf3d5 | -5.97352 | -57.76495 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21315dcd-0e9f-39ea-9a8e-9a26b6d7f0eb | -6.83886 | -59.3566 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e710f9ac-ae0d-3170-8a1a-a9b74ad00341 | -6.84264 | -59.36143 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d506944e-6c41-3e24-a926-d8633b987ff1 | -7.39224 | -64.57201 | 2026-09-11 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 953eb841-c9e8-38f5-81a0-b6bc262d6964 | -6.19481 | -55.27598 | 2026-09-11 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02d68229-ff4a-33f2-a78f-34fb1ed8fe5e | -6.23726 | -51.69688 | 2026-09-11 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5bede6e-9151-3a0d-bb3a-3f4ebaa7f1f2 | -6.19595 | -55.26793 | 2026-09-11 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1059e1f7-442f-31ef-af56-558332773a4f | -6.19996 | -55.28084 | 2026-09-11 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 031782bc-e618-3e21-bc90-b7ec62f2cd3a | -5.97833 | -57.76576 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fe4cb87-c386-3e2f-9df2-7eaacad418f7 | -5.36976 | -56.02294 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91708168-6477-3486-830f-e489f46dac95 | -7.84962 | -56.58821 | 2026-09-11 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1bb4fe2-98d7-32cc-ab03-8fb113c5ff5f | -6.83826 | -59.36077 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80b4f42-0e72-3f5a-ae13-75fe7179c281 | -7.42298 | -64.61687 | 2026-09-11 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a93eb99-fe30-33ab-bc07-7bc603966a2a | -7.39846 | -64.64214 | 2026-09-11 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 591b348a-062d-3891-beb0-eb8757547dfa | -6.1108 | -57.63657 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51586b76-3fc7-3eb8-a7ca-32dea412e545 | -6.05329 | -57.79211 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef74e280-e34f-30e0-a35f-6a86b1ab7d2c | -6.76908 | -59.43385 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bab61407-c704-31bd-b66a-3dcbb054e8cf | -7.24643 | -59.52116 | 2026-09-11 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f49e20e-614f-3840-8a30-82932f5a4824 | -5.9768 | -57.77671 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b81c9700-a647-371b-b388-5597a768e7c4 | -6.50435 | -58.38848 | 2026-09-11 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6fc1186-24ef-3493-ae7a-b5adf73764b3 | -5.97276 | -57.7704 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef8b23d8-1430-3af8-abbb-e8070ebbce27 | -5.36734 | -56.02267 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e85f2125-5c8a-3a2f-b2dc-44601adc0576 | -5.9739 | -57.76896 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c14f5f51-a24b-3a16-b5ec-f9963047cf63 | -6.1088 | -57.63709 | 2026-09-11 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c69eb00-e7f8-3d4b-b764-897ca9d91e56 | -4.53757 | -54.96148 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b7f30ab-7c8d-3ef6-9f80-20afcf36427d | -4.83106 | -55.76341 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 686fe5e2-a904-3ce6-9882-7e7c6ab059c7 | -3.13229 | -60.66162 | 2026-09-11 05:48:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 862dd2e9-2588-350b-a41e-2fb474a4f2dd | -3.4183 | -59.22992 | 2026-09-11 05:48:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f71fd93a-e717-385c-bdcb-b859dd6b16cb | -3.14971 | -60.64994 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2cb7df-ba42-3efd-bb6e-3c7386652416 | -3.65967 | -58.89858 | 2026-09-11 05:48:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a7e755a-bccb-3538-ae3b-14b589a95bb2 | -3.73633 | -61.7552 | 2026-09-11 05:48:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 62d67511-e479-385c-be5c-69f5a04967db | -2.72116 | -57.62785 | 2026-09-11 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89a51a50-2fd2-352e-8bbd-f88ce49b875d | -3.15278 | -60.65522 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2b7f21a-5714-3f13-8d04-8ea039118ec4 | -3.39621 | -54.08326 | 2026-09-11 05:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a30ea956-1ca5-32f2-809d-406a9983c9fd | -4.83057 | -55.76678 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a213168d-27ff-3c44-b390-f866acace130 | -4.86453 | -56.00738 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2f8e9b2-428e-3a81-8371-24bc55817908 | -4.53067 | -54.96878 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feefd0da-1dbe-3cec-81be-11bdb8b81b90 | -3.334 | -59.43747 | 2026-09-11 05:48:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6b6224f-22e1-3ecc-97d2-6309946e64aa | -4.86394 | -56.01147 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ca0ffd-9e98-381a-bac8-977133da44c4 | -3.1361 | -60.6622 | 2026-09-11 05:48:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ec8cc747-0aa4-30f4-9728-6dc181188b6e | -2.72725 | -57.61896 | 2026-09-11 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90a29dc0-7a7b-3f1e-844c-033c7f71535a | -3.15659 | -60.65581 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec8fe1d1-b13b-3f51-9056-67d9f676282c | -4.52615 | -54.95988 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae7fb1db-085d-304c-a29d-8030aad849af | -2.72189 | -57.62305 | 2026-09-11 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92087c10-36af-32db-8f43-1cc56a2f76ea | -4.86509 | -56.00344 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eda4b15e-9a67-324a-bce4-907ec3a77576 | -4.83008 | -55.77015 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0ca4ece-3739-3b5b-9d4a-5c87a3d33423 | -4.53187 | -54.9606 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e3307b7-221d-3004-b43e-0a89093429ac | -2.53363 | -59.55236 | 2026-09-11 05:48:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8ae0732-0f3e-3f5b-bd21-4ace63a60c3f | -4.52559 | -54.96368 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b2a5679-fd05-3c59-a019-bc095f0248a6 | -4.86943 | -56.01128 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b47ce0a-e759-3ddd-8e83-8762ad1097c4 | -2.71945 | -57.60794 | 2026-09-11 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f006682a-1455-3d9c-a30a-84c18354949d | -3.1597 | -58.64791 | 2026-09-11 05:48:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92807eff-7fb9-3922-a15b-7928d1339b6f | -3.17419 | -61.18669 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d4c4b0-9309-318c-b9da-341b9b91844c | -3.39882 | -54.08238 | 2026-09-11 05:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11d089d7-841b-3b19-a8d7-2c4b860ecf0f | -2.72262 | -57.61825 | 2026-09-11 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bde268f6-787a-3af9-9ab3-3f128ea7ebcb | -3.16247 | -58.64919 | 2026-09-11 05:48:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f41696a-e2a3-334c-bd82-56e18741547c | -3.33813 | -59.43808 | 2026-09-11 05:48:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c9cb53-b249-3002-82be-d9a94a17517d | -3.13737 | -60.62888 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9dc3ff0-872f-36de-8e80-60bbe27f8c99 | -3.39685 | -54.0788 | 2026-09-11 05:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bafc52e3-d4e9-3b95-aedf-cb504ec44427 | -3.77119 | -58.84711 | 2026-09-11 05:48:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53a6e8ea-36f5-32fe-94c7-02204cc98bce | -4.35655 | -54.77958 | 2026-09-11 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 447ea3d5-f796-3fd4-aa63-8b28b47e26c5 | -3.73994 | -61.75575 | 2026-09-11 05:48:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a0be44da-acc7-3b9d-a2e9-0145791d6f4b | -3.15351 | -60.65054 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dea8ae1f-638d-3d6c-a6dd-677af9bd947c | -4.52094 | -54.95564 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b0ae7f3-5094-3e44-a136-d3b37c467d43 | -2.74469 | -60.23825 | 2026-09-11 05:48:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0041ee51-86dc-35c5-866a-8958e5445d14 | -4.86997 | -56.00754 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa29c35d-6dfa-3fa8-8b25-aef32f408def | -3.39949 | -54.07798 | 2026-09-11 05:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfda52bc-8c7c-3aee-b5a8-5fa557fbd1ca | -3.13226 | -61.47849 | 2026-09-11 05:48:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 584d9e35-0459-335f-958e-132c6c1f42e9 | -4.85913 | -56.00696 | 2026-09-11 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f80f1ac-5973-360d-8f04-245cb6673693 | -3.15732 | -60.65115 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README32.md)
