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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdb5dc72-fc4a-3ac2-aea0-470a840989a0 | -3.38237 | -58.19653 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d8f161f-ad7e-3f27-8943-29598f8f7c7a | -2.788 | -51.68299 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ac1e63e-b712-39e7-998b-3f0b4b328e41 | -3.56774 | -54.48681 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b159f24-6eb1-367f-8fa9-ba17f798c89a | -2.97767 | -54.1299 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccb85edb-219c-374d-8ad9-a37681433423 | 2.43759 | -50.84982 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30111370-5517-32a7-9ede-2266b64286f6 | -3.50651 | -54.64721 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b714bdc-2b23-339a-9054-8d9b36df6d33 | -3.48801 | -59.58082 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d24959d8-728b-34d1-9306-cccb6531510e | -3.49907 | -54.63381 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db7b21b9-6abb-3a88-bf8f-00549b9efbfa | -2.99388 | -51.04842 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 546828d9-9723-312e-8746-4c69eb8a7de7 | -3.05493 | -54.2681 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db36c7e8-1714-3903-9ec3-ebbb72fa693f | -3.54842 | -59.48356 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 659f83d0-32c3-3cf7-8a82-f28adb7e9aaa | -3.28551 | -54.02486 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 32cd7bc7-e49d-35cb-b4f0-4e2a2e4e2f84 | -3.05748 | -54.15541 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01b28976-b910-3a23-97bd-88f0af886fee | -3.6181 | -55.28445 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d36e9952-741e-3aa9-a40c-2d7af3196263 | -3.17667 | -50.57073 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7ba51023-19ae-3a0e-b75c-01cad4623c3d | -3.2463 | -57.86877 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3c50c9a-7fe6-3170-8c84-ee3770430f48 | 0.70553 | -60.51008 | 2026-10-07 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b78ea9a-7e74-3fd8-bed9-adbbefde6244 | -3.84588 | -55.98526 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6f37b1ff-ccc7-37c1-b677-178dbd518c47 | -3.07327 | -54.17781 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40eca960-188c-32ef-97bb-e60ecafb9816 | -2.93666 | -54.16712 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb515986-cf9c-3518-9975-849a7c9f9105 | -3.65141 | -54.05744 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed80c148-654c-3496-b940-7ada48263d47 | -3.84463 | -50.31201 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be7acdca-3798-3b93-87f3-6511082b7da3 | 1.29363 | -54.70404 | 2026-10-07 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74968fbf-260f-34cd-9163-b0e1abbdacbf | -3.54267 | -59.49789 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6008d29e-d297-3e3b-b4f9-083ac2a1429c | -3.09893 | -53.74413 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c00c40fe-c190-3b23-80df-6f2078c7c9ac | -3.99617 | -56.26147 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 489d8957-1953-37bd-a41e-389a24e513fc | -4.45386 | -47.91298 | 2026-10-07 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dcf05888-8060-32b3-95aa-5fcda8beca54 | -3.04232 | -53.9269 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40908c8b-9d36-3023-9781-77dc1edd269a | -3.50983 | -59.95324 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd589c0f-03c2-3cbb-957d-4ff8276d1347 | -3.27766 | -50.13907 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1032d033-6719-3964-ab13-49d5415c88e7 | -3.26972 | -50.39985 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15dec1a-e1f3-394b-8b68-2dfbad45fdf5 | -3.21591 | -53.87421 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc7acfb0-9370-3bc6-a128-68be8be90f6e | -3.22632 | -54.3026 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a30e93b9-c9bd-3699-8bd7-fca4ceadba1a | -3.01583 | -54.13109 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd571786-8a4c-3ac8-8221-76cff41c767e | -3.22394 | -53.88596 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87ad95ac-619a-30f9-9dc5-bf34e1c79b6c | -3.49985 | -54.66013 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d238ba8-e1fe-35b1-9938-a7ecbe5883d7 | -3.05998 | -54.17075 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd14a0c1-be5f-3340-808a-48646caae8cc | -3.28397 | -54.04177 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87ca1543-5e6c-39f4-9225-95b07fa98fa9 | -2.75897 | -54.09337 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0f53ffcc-0db8-3c97-ae95-e1fa990b83cc | -3.28082 | -54.05493 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e891b9f-a1a7-332c-8d82-9768e167df38 | -2.90135 | -54.11708 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6119b675-830e-3189-a703-809562434de1 | -4.34789 | -55.16618 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12337bbb-d6b7-31cf-b678-86726ead8a68 | -3.38897 | -58.20182 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33fca0f8-b70f-3cf3-af89-fa6e7fe5decf | 1.80177 | -55.53234 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da19a3e3-9fe3-3b1c-a55d-cf5a6f93f2dc | 2.1289 | -50.83007 | 2026-10-07 05:40:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60aaddb2-70f4-3bc3-ac2a-b5d316a61c64 | 2.43817 | -50.85321 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecdc444a-e130-3130-aca3-ed5477ced09e | -3.24261 | -57.86821 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04e6ec8e-68f1-3762-8745-34db58c6cec2 | -3.5691 | -57.80183 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d8b7f69-42b7-3c24-9572-beafc6e27254 | -3.47797 | -59.48834 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a161371b-1d1e-3caa-8e32-6ea90e64cdee | -3.8584 | -55.98727 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be090f94-43cc-3ce5-a976-2e365210bf7e | -2.76365 | -54.09407 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f58468ba-d2d6-3ec6-940a-2a8e05093d3e | -3.85062 | -55.98215 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3775247c-7bcd-330a-be0f-c50b07aaccb4 | -2.96144 | -54.14235 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2be5171-3d28-36d8-b03f-6f0c6f5db9f6 | -2.93907 | -54.16411 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aac025ad-fd1c-3476-9e08-a3cd239615c2 | -2.99835 | -54.18272 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ebb3017-c0ad-33d9-898e-840d6643f0a0 | -3.27775 | -54.05108 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d85a76ae-f848-3714-9c0a-3615e4d056fc | -1.34127 | -55.45948 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a4f507-9020-3875-9b97-49f60f88106a | -3.05027 | -53.9385 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cef5d61e-3838-3405-a002-c8a348996630 | -3.74354 | -51.21583 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42068784-5ac6-3130-8f5e-0dddba66f70e | -4.26752 | -54.865 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4e04768-5e06-35d4-a756-7278b78698b5 | -3.84949 | -55.98969 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 639ec036-488b-3575-b1ab-796117122617 | -3.10906 | -53.77998 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d9986b5f-b742-311c-a7ba-6360decc2687 | -2.86941 | -54.20126 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba1121df-701c-3baf-b2b4-db7ab55ec2da | -3.08442 | -54.29288 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 50fedc64-6380-344d-89e7-b531d1fad0fb | -1.80592 | -57.11019 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75c7fea6-1ce5-3454-a8a9-bb56a586b77b | -3.09737 | -54.17656 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aab8a3fd-5054-3aeb-bf21-387135f7d455 | -2.5301 | -58.09406 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f10c9095-3628-39d2-b7b9-e9c0aacc856b | -3.38905 | -58.20088 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2269e89-a624-305e-8625-285a61f16605 | -3.62745 | -55.28178 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11052484-f720-3050-a56a-2912345cfb78 | -3.59018 | -55.56281 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ca94076-058e-32f1-8b7e-d48ed4a804a0 | -3.47862 | -59.46181 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 685f707e-64c0-36fc-965e-49b7b33434a0 | -2.99784 | -54.12333 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a6f2c031-5d71-303a-aaf6-de07cbe008d4 | -2.91298 | -54.10377 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f955cb-bc08-3abe-bccf-6865f6237e7b | -2.73903 | -58.18682 | 2026-10-07 05:40:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03342823-f766-317a-8c50-961aaa78df00 | -3.20636 | -53.87257 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c33e82d9-9242-3ca9-b0f6-fa2e363a5b5c | -2.78873 | -51.6801 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8a33a37-3cd0-354d-b34e-a3e8b87957ee | -2.03503 | -57.05167 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2478446c-2919-3271-a590-fda820b8bdae | 2.44302 | -50.83108 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fa54b09-999b-3413-a6e5-3691da3c0bbc | -3.37893 | -59.43185 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab9c5a5b-4e30-3d24-a96a-621ae5b9c3ee | -3.68315 | -55.94947 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a96c13fe-7cbd-3b17-be35-8e61c565f4dc | -3.65317 | -53.50341 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa888d79-4a85-3f48-9696-fd8b3396c4d4 | -4.09939 | -52.07217 | 2026-10-07 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 679ff65e-9836-3fbf-9b09-a7b21b1b7da8 | -3.21036 | -53.87862 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| defd1893-f4d1-3da3-a85a-806b6ff7242e | -1.28252 | -56.97944 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a2190a5-010a-3806-b64e-795a1dce70d8 | -3.22356 | -54.30019 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49ed1ddd-f053-338f-83b0-3ccdebef6ac6 | -4.14745 | -54.03445 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 870085ae-3114-3680-a746-d8ac9e21aa38 | -3.56102 | -59.49312 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a26281ea-74e7-338c-bd0a-7c413aeaa67c | -4.26618 | -54.87402 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9860155-17fd-360f-a594-0a6331cc0eca | -3.04892 | -57.52085 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dd5af19-5b4f-3842-a4f2-64bfb69aa605 | -3.05675 | -59.90575 | 2026-10-07 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a022d152-9668-3dec-8479-29573c0ee8eb | -3.13169 | -57.82421 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6a41526-df08-3d75-a127-e449b6fd991d | -3.00196 | -58.89516 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79e3f5f8-6cf2-368d-a4f7-54c4501bc487 | -2.9397 | -54.14769 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 374dac33-42d7-32f4-b42f-15d7cfd04b5e | -3.50481 | -54.62809 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85f9d2b9-b99a-3173-a4ad-630902b5c24f | -3.50343 | -54.66745 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1c91c2e-dcfe-3e9b-b567-3f4bb7e4dbef | -3.549 | -59.47984 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f2f32ae-f103-3b8a-9f74-e4b13318c9cc | -1.29651 | -54.55954 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56f7abf8-7936-3507-a1fa-af3579cf9069 | -3.04634 | -54.15071 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20c563d4-3538-3ff4-aba5-e88d0422a1b6 | -3.98533 | -56.22243 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3c94402-6170-3047-b53d-26d7eb71318b | -1.48137 | -54.84186 | 2026-10-07 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README105.md)
