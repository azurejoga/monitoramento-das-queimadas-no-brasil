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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5b07dde-6293-3281-b25f-ac6b5fa5000c | -4.7328 | -55.67033 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf431bd0-db9a-3497-ac7e-b3614575ad0e | -3.09727 | -53.93619 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acce41dd-b561-3fc3-ac41-995abb0108f3 | -3.46649 | -50.59058 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93c99fe6-a815-301a-a6b0-47829cefecfd | -3.7452 | -55.95243 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ff2fd05-4665-3591-a77c-07f787617ae6 | -2.47259 | -56.0868 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a632cfc6-a4cc-3d0c-bcb1-d60fe30803cc | -3.88932 | -52.19085 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 723fe1bf-539d-3d95-8dab-f6499e880df6 | -3.98756 | -59.35546 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6060f83-527c-3ee1-a199-99705f6b6044 | -3.49056 | -43.3387 | 2026-10-10 04:44:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e98613d-a561-3267-9ef8-0f713886ed3c | -3.62843 | -54.23822 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4a63571-f67a-3359-a57d-57e63eeada90 | -5.75131 | -45.13419 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf2d63e6-fc1d-31d8-be63-748f557c86ed | -2.22289 | -50.48899 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 77591647-a0d8-39ae-8382-5de949fd3c5d | -4.15428 | -43.18406 | 2026-10-10 04:44:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ff9e6e2-d267-3183-8f72-ef0596f338c8 | -4.1167 | -50.97797 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 781e150f-2662-3915-aff0-5c3ca58ee8bf | -2.88814 | -54.07481 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1bfc8ef8-23a2-3ee7-b848-c1ef05709a09 | -3.84783 | -55.79085 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 26f3352c-da34-3a0b-a6fc-7a06e5eaa249 | -3.20764 | -53.86085 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e261bca1-51c2-3a90-b123-0881b434584d | -5.23813 | -45.37376 | 2026-10-10 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 763efeb9-a92f-31c1-b7ed-fe26bb6efa7f | -6.88373 | -45.91509 | 2026-10-10 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb1bccd1-266f-3326-8e72-b3287b044ba0 | -3.24893 | -50.42316 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef25013-5124-3942-9af6-ee2c499eab33 | -3.00265 | -53.91346 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fea5c574-5ed1-3e56-a0a7-edda717bc8b6 | -3.15733 | -50.59046 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d082b46-ea28-3726-af9c-c5a18d704bf5 | -6.91142 | -45.8732 | 2026-10-10 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08083907-47bb-39b4-bad2-0a86f26c976b | -6.05781 | -44.65771 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d853536-ca97-3215-bb79-1f680b7c236d | -5.04746 | -49.35154 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86c5909d-1619-3f01-bba8-ee44730541a5 | -4.7299 | -55.65686 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08c76b27-010a-3c12-b967-71e7840bf4f0 | -2.73191 | -54.13595 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32515000-a9d1-39b9-9abb-544f879490fe | -2.85188 | -59.12505 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32122885-ea55-33f4-83fd-6b750959607c | -6.88432 | -45.9113 | 2026-10-10 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37642772-ce4c-3f47-b62a-d9d4e3f89fe3 | -4.11431 | -54.01423 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa2c1c07-4e5d-3764-88a9-e4bac2410f07 | -3.07663 | -50.96592 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54ae1596-163d-3792-9ff2-c41c5cbc03c2 | -1.1138 | -54.17071 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a11d0df1-316d-395b-b776-6db93ee6bee0 | -4.09325 | -53.99844 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 545fdad4-c5f7-3871-bfea-57577573ec65 | -6.07096 | -44.66827 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de5e01f1-657b-3a16-8b31-3b1783c2f5fa | -3.87891 | -55.98902 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad10d6c6-2f9a-34bc-9670-8c4c682a4c48 | -5.13042 | -45.79473 | 2026-10-10 04:44:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98fb3ea4-14d1-35ce-a60e-fd89b741cc46 | -6.06078 | -44.66247 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c2a2b8f-4f9c-3397-8b0c-2ed8b25a360f | -5.69806 | -53.46785 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96cbed44-27d1-3015-bf01-33589c7200b4 | -4.09849 | -53.9971 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7bb24f2c-067a-3573-ab6f-ad2dc5a76d4d | -6.9653 | -44.95696 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03000cf7-5652-3260-b4e5-736ee14b0420 | -3.29739 | -53.99931 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db9de01f-9277-3152-82f1-9d79dcf8d90f | -3.31529 | -53.83414 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbf7a8f8-cc54-301f-b4e3-3b6c53769609 | -2.8936 | -54.0707 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07bec072-d794-384e-9821-bad668b2d2f2 | -1.01247 | -52.28373 | 2026-10-10 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4019f494-4ec5-39bb-88be-182842219afe | -5.6922 | -53.46575 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bf7a0cf-3f5e-3415-9855-3c490a095836 | -5.70291 | -53.48019 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73861d5d-d83e-3643-8d6d-ec85a8d79a30 | -7.20919 | -44.3508 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3c45c5a-e6e2-3e21-b7f6-503e110d70fa | -3.99216 | -59.36737 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3cf4f5e-35d8-399c-b539-dd419b8c4032 | -3.20278 | -50.82999 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de4c0e1-2406-3200-b589-94316012d67f | -4.5956 | -50.97543 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1207bc71-d6c8-3267-84d2-29c20a94b091 | -3.03803 | -59.16183 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a498f5b-030a-31b6-8662-2e6fd135a210 | -6.45389 | -43.45162 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4e4301b-a191-35b4-a3a7-859bf85c8585 | -3.54201 | -54.73879 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5f61b18e-b87e-3927-9d5e-2fd1e56d2d0f | -3.11906 | -54.16405 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 701ca3ae-0b2f-37eb-b3bb-ea27764eebe1 | -5.6576 | -44.35062 | 2026-10-10 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e626906-b572-3639-afd2-37487cc9ca9f | -3.11189 | -53.79022 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 901ffc55-2b2f-3acf-9605-c0b7dbec8f61 | -3.55939 | -54.69298 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b9ad9d8-8425-365e-b862-dfa8d0034616 | -3.91792 | -55.82051 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f940fc2f-c969-37ae-8b4b-8683704d3144 | -5.80119 | -53.79553 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d659ccf0-6ba2-372b-bffb-18d8cad98c3c | -1.10898 | -54.1698 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 096ed849-4dd3-300a-9e78-63c3bcb861f1 | -7.21054 | -44.34181 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fa5393f-913c-3d54-8db4-36a41b5afb45 | -1.63961 | -54.39316 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77835cdb-834f-3940-a0e7-5ca97c0f7a74 | -1.27073 | -55.7497 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73b1eef5-5028-3244-b73e-342fed58f952 | -3.39342 | -50.21917 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4adb46ce-2e5f-3ae8-b526-85c04ba906a1 | -3.22687 | -49.4353 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| c2c42843-c2a2-30e2-b691-ef8e42df831e | -1.95489 | -54.40691 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d02d748-10ba-3a28-85e1-76758c8e0758 | -2.76101 | -54.1055 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc7eb477-ee62-387a-a667-be91c3b9f6f7 | -4.09912 | -54.02086 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 290f64b4-18ce-3fa4-b212-27cd8beb04ac | -2.2187 | -53.69676 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c1fdfc6-d219-3edd-9804-0b0f117ade93 | -6.81776 | -39.55393 | 2026-10-10 04:44:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c039213-5aa6-3b84-84e5-43874f16834f | -2.97686 | -54.07119 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73217120-9c61-316a-bb1c-78cf8220ab25 | -5.70787 | -53.47701 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51f6d984-aeba-3595-8654-b438f33ff70a | -2.60752 | -56.48706 | 2026-10-10 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eea766e4-4fa2-3f93-b86b-a9c874a757ca | -6.64397 | -47.91482 | 2026-10-10 04:44:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e335f37-e2a8-30fb-841e-0e55d0323ddf | -3.31753 | -54.67595 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 614407d7-145b-3a86-bda4-c22282733409 | -1.02046 | -52.42828 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfaf2aa3-f9b6-397a-8932-0141f47630ef | -0.87576 | -48.71217 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4605c50-a091-3018-a939-254b53146cf0 | -3.75248 | -50.00425 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 679a5ad2-2d37-3311-84c2-22d2eb09ad1e | -3.19235 | -58.64467 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dd01c4d-c85f-3e5e-a520-148b9d9914db | -6.51241 | -45.40508 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a5f715b-6b64-39cf-86de-37236438b113 | -2.92315 | -54.07721 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 181a9af6-5271-3526-bce4-649726e55c3e | -3.16104 | -50.59106 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e05671f-966d-3d11-ab58-4885cb1ffbfb | 0.48991 | -50.7891 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3469064f-c1a0-3e5e-a4b6-f07345e4fb6c | -3.49843 | -54.61326 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fbb734f6-7884-3f2f-aaa7-dffb7fea8123 | -2.93572 | -54.05937 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdee3d38-35c1-3e09-ae51-4fa8e8c187bf | -2.61424 | -51.7071 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b931e699-1bc7-3a8e-a8a2-047721ea14a7 | -2.74432 | -48.4275 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 875b914b-6841-3e88-8d5b-8e2b8a0f621e | -3.21983 | -48.81544 | 2026-10-10 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9616538-af13-300c-ba6d-c59c324b2317 | -3.87316 | -55.9912 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f82d5e72-e868-318e-aa66-c13bb6559ad1 | -1.87632 | -56.31013 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0743451-6b5a-35bc-bd17-ae1394d56def | -3.858 | -44.04361 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2666a3e-1d24-3963-844b-3f93ec1f375d | -6.1302 | -43.53254 | 2026-10-10 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9d7796b-edbb-3bed-a27f-579318f0ccbd | -5.66124 | -44.3512 | 2026-10-10 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e1ec678-c060-39a1-b7d0-e29521a48f14 | -2.99959 | -53.90321 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8df315d6-fc0a-3d38-9819-af2a607d1aab | -3.00994 | -51.01659 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dee7c9c-d0f9-3354-9597-e253b24955ed | -3.01128 | -54.1091 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349775c2-aba7-34e3-bdb8-58d63c9bcce6 | -3.49936 | -54.1952 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65cadff-8d95-3748-a532-3d679e8715cb | -4.08076 | -44.92045 | 2026-10-10 04:44:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca3d914d-81ff-35a5-ad73-b70826f7dce9 | -3.25559 | -50.42867 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d38fcb5-9f3e-3e57-9e45-03ce512f91c0 | -3.57636 | -59.08295 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64f51898-44df-3551-ab0e-cf25df73bebb | -3.3476 | -50.48098 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README67.md)
