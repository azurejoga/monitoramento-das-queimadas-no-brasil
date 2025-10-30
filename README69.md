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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce2e9e0-f69f-3629-8c34-a70c08c9b3f5 | -5.8152 | -40.8296 | 2025-10-30 13:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 81fa308c-c668-3018-a71d-eb674d139f5c | -6.1462 | -41.5996 | 2025-10-30 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 3bcc121a-41c8-31b8-b56a-4797418fadee | -3.3561 | -44.2654 | 2025-10-30 13:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f7ef731a-58bf-3213-937a-2f5070313442 | -4.2544 | -43.7149 | 2025-10-30 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 842505be-1442-3104-9973-c51d81b94b73 | -3.7867 | -43.9011 | 2025-10-30 13:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 25513be5-00e7-3172-8455-af9fa0a4fa91 | -6.5794 | -41.5841 | 2025-10-30 13:40:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 7caaf16e-30c8-3115-806e-87f412f82769 | -6.2785 | -45.3169 | 2025-10-30 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d2678dba-dec7-38ea-8314-2cc5d364acd9 | -7.6302 | -43.5895 | 2025-10-30 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 28b4867c-2dd9-3cb3-a9e2-aeddfb4cdd4a | -5.8152 | -40.8296 | 2025-10-30 13:50:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 9a354633-a865-3b61-a01e-229d80e95f7c | -13.5876 | -47.3438 | 2025-10-30 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| edc96933-2dab-33a1-91fe-97fbc55aa3ae | -4.2544 | -43.7149 | 2025-10-30 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e28ce41d-fe01-3c3f-ae35-23cdce1ea39b | -5.5298 | -43.2371 | 2025-10-30 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 132f90f7-1c9b-33c2-be03-7675977b4670 | -5.6092 | -47.1253 | 2025-10-30 13:50:00 | GOES-19 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 27e1aa7b-eddd-3984-ada1-24bdd56ff70a | -3.9949 | -43.4279 | 2025-10-30 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 32a7e1f2-7cfd-3127-8fc7-b1411708264e | -7.6305 | -43.5661 | 2025-10-30 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a9fe992b-d111-360f-a7ca-1808271ec2da | -8.0212 | -42.5121 | 2025-10-30 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 09528618-e6b9-3991-baf9-dd86af6bbf47 | -13.0446 | -47.5379 | 2025-10-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3374a9be-414b-31f5-a931-c57a7e2e2d02 | -7.6111 | -43.6147 | 2025-10-30 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 87a37663-2261-3c74-9a5c-dfe432440e79 | -7.6299 | -43.6128 | 2025-10-30 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 673ea882-f5e0-3718-be4b-0febd48c39d0 | -6.1464 | -41.5755 | 2025-10-30 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 366461b0-4f55-319c-9eda-c591ab5f1fd5 | -7.6114 | -43.5914 | 2025-10-30 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| f9d42a74-f9cc-3769-921d-89af511e9720 | -5.6643 | -42.8755 | 2025-10-30 13:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| f7061b20-9914-3f26-a213-9c781434cc07 | -5.2496 | -40.9731 | 2025-10-30 13:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| cf8b3521-61d4-34b8-b730-73a1353d038b | -5.6992 | -43.1541 | 2025-10-30 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 132.9 |
| f998d70e-f46a-3195-91ce-7125c7adb3e2 | -6.0461 | -44.1484 | 2025-10-30 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d8fe84fb-88c4-3692-973d-0b475787e372 | -12.3297 | -50.1586 | 2025-10-30 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| e9d02ad7-6ca8-3d91-9719-2b3ba207c232 | -7.6116 | -43.568 | 2025-10-30 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| becc682b-be7c-3b13-be65-52bccc331bfe | -13.725 | -43.4529 | 2025-10-30 13:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 8ba8b0ed-44bf-34d9-8907-c256ac9c2a62 | -6.3787 | -40.9737 | 2025-10-30 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 4c1df9b0-8dd1-383c-8e42-0acfc74e3d82 | -3.7867 | -43.9011 | 2025-10-30 13:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 9549dac3-07eb-3a05-814f-c54d46a09b8a | -6.5605 | -41.5859 | 2025-10-30 14:00:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| f0ccf067-3be8-3f18-9a41-3cd53233bfe4 | -7.6305 | -43.5661 | 2025-10-30 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9884fdb4-0ba2-34f5-9ef7-4519b3cb2754 | -7.9215 | -46.0094 | 2025-10-30 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| d758ba74-6749-3577-ba59-79db2e15b088 | -7.94 | -46.0301 | 2025-10-30 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2a8b3d71-6572-32c0-83f7-4e8345e5d579 | -8.2042 | -44.4343 | 2025-10-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 0530de01-ab26-3653-b2fb-c4ae8d9a55ea | -8.0633 | -45.1587 | 2025-10-30 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 43bb7760-a6b1-33db-b52b-b2b6c975c486 | -5.699 | -43.1776 | 2025-10-30 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 85.2 |
| b8c07034-b855-3415-ab60-045e95ec1e50 | -7.6302 | -43.5895 | 2025-10-30 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| c27316ad-4ea3-38ba-90dc-50532f33e7c7 | -7.6299 | -43.6128 | 2025-10-30 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c614e5e9-3c68-30cc-84be-1dfd90892dc7 | -3.9949 | -43.4279 | 2025-10-30 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 914a9bed-2e81-32f5-8131-86f923bf71d3 | -4.2731 | -43.7139 | 2025-10-30 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 0ded97da-055d-353e-b703-bc6e1f0074e6 | -5.6994 | -43.1307 | 2025-10-30 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 17f17b6a-5195-329b-9763-cd928881079c | -12.9323 | -47.3752 | 2025-10-30 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9ca782fc-bfa5-3da6-9ee6-da92daac124e | -13.0442 | -47.5603 | 2025-10-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| cc2bb888-bd2d-302a-a9a5-973956651f63 | -8.0444 | -45.1606 | 2025-10-30 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| cbf46c76-571a-3783-acc3-87b272c72cf8 | -5.8152 | -40.8296 | 2025-10-30 14:00:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 98.6 |
| a28c303b-575f-32db-a8f5-c395c4305d2e | -3.995 | -43.4047 | 2025-10-30 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d0eeee1e-a6b7-3b3e-95bb-ccb3f9ade49e | -4.2544 | -43.7149 | 2025-10-30 14:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 3e30aadc-4ba7-3c36-a2f8-ed764491a71c | -5.2496 | -40.9731 | 2025-10-30 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 178.6 |
| f31d60fb-290b-334c-bfd3-98c3c5ae9246 | -6.2758 | -41.8042 | 2025-10-30 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 0e691f51-cf72-3b07-b073-fb6fb0ef9d61 | -6.5794 | -41.5841 | 2025-10-30 14:00:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| e5b35a99-5188-3a06-915a-47b195c5763b | -13.0446 | -47.5379 | 2025-10-30 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 90145ebc-8895-3987-aed5-5ab1d77b4733 | -7.6114 | -43.5914 | 2025-10-30 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| e7739180-3875-3241-bb79-edb083a7fc95 | -8.2039 | -44.4574 | 2025-10-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.8 |
| e8949f7f-e4e7-3537-a8f9-3135abef7a60 | -13.687 | -47.1932 | 2025-10-30 14:00:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0726307e-b768-3d68-a57f-009313b0825f | -14.3091 | -48.016 | 2025-10-30 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| be4a5053-fefe-334a-b2e4-55dc782617ec | -3.8605 | -44.0355 | 2025-10-30 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| e861db9a-dee5-364f-bbdd-a633d9c6d28a | -3.7867 | -43.9011 | 2025-10-30 14:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 1f898c3a-f955-3ce7-a780-77c8a4e0c275 | -6.2755 | -41.8282 | 2025-10-30 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| ffa0f0dd-484d-3dcd-b229-ffa4004468fd | -7.6116 | -43.568 | 2025-10-30 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 0b48882d-73e1-3d78-abf3-d209523b9e6d | -5.5298 | -43.2371 | 2025-10-30 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3a8e4fdc-e644-3aaa-b0cf-55758a025d57 | -13.0446 | -47.5379 | 2025-10-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| be6170a9-4060-31db-b11c-f13e80be3711 | -13.0442 | -47.5603 | 2025-10-30 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3b1b2113-52a0-3f6c-ad99-89159677126d | -6.5791 | -41.6082 | 2025-10-30 14:10:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 9558f33b-35c6-35cb-b90f-4a1ba7903a79 | -12.9323 | -47.3752 | 2025-10-30 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8c32376c-7cd1-37f4-9812-e2fe667eb37e | -7.6111 | -43.6147 | 2025-10-30 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5be8fe25-7899-3d9d-9db2-59dec848ad30 | -4.2544 | -43.7149 | 2025-10-30 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2a5cfbea-e5d1-320a-81b6-77bbdab04505 | -8.2039 | -44.4574 | 2025-10-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 692448c2-4932-342a-b1b6-4d07d411f65d | -5.7963 | -40.8312 | 2025-10-30 14:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 3932f40c-e527-3d12-8c70-955dc718a6df | -6.7126 | -38.217 | 2025-10-30 14:10:00 | GOES-19 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 114.0 |
| cfe165ca-0481-3651-ac95-aec8d9a90038 | -7.6299 | -43.6128 | 2025-10-30 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 022e2f9e-844a-3a07-973f-582ef99beed8 | -8.0636 | -45.1359 | 2025-10-30 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 56e94da9-8578-35d3-841a-ad82103f2381 | -7.6305 | -43.5661 | 2025-10-30 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 8353cad4-3681-32c0-b1da-801db6b480f8 | -6.5794 | -41.5841 | 2025-10-30 14:10:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| bbfe2709-533f-3321-9f3d-babb7ca3e9cd | -8.2042 | -44.4343 | 2025-10-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3f9822d6-5004-383d-b374-c74ec6fac7bb | -13.5876 | -47.3438 | 2025-10-30 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 98348897-b5b0-3f4c-94fa-dff2d9d6eab2 | -3.8605 | -44.0355 | 2025-10-30 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 83d634d8-e061-3e0a-af3a-b8f3edf24bd8 | -8.0444 | -45.1606 | 2025-10-30 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 924a19f9-6dc9-3da6-9cea-e0c925c4dc4f | -7.6114 | -43.5914 | 2025-10-30 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 9844684d-5d57-3291-b35f-d9bcd5fd2769 | -3.995 | -43.4047 | 2025-10-30 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 277121c4-b222-3fa0-8a8e-560c9e8d8cb7 | -7.804 | -46.4234 | 2025-10-30 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 810c793f-aa19-3151-b8fe-ed24bbb17eac | -5.2496 | -40.9731 | 2025-10-30 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 151.6 |
| e13107c5-a940-3697-8496-5c7c77ecb3cf | -8.0633 | -45.1587 | 2025-10-30 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c16f7fa7-046d-3f7f-a43a-b83f2198db7f | -3.9949 | -43.4279 | 2025-10-30 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| d514206c-ec4b-3785-a461-946176f6566a | -3.7867 | -43.9011 | 2025-10-30 14:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ec0ac26a-24f2-3358-9275-3222f594dfbd | -7.6116 | -43.568 | 2025-10-30 14:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 58f78518-e3ce-3173-bbfb-8b94a7deb90a | -8.5652 | -45.6975 | 2025-10-30 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ca92997b-6e7d-3c4a-a096-49e9db78f646 | -4.2731 | -43.7139 | 2025-10-30 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c2dc65e7-b661-3760-87d4-9861d121fed3 | -5.8152 | -40.8296 | 2025-10-30 14:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 88.7 |
| d9893236-ed00-316b-b934-a97f076cb4af | -10.2663 | -44.5603 | 2025-10-30 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| d2d7e7f5-6f7d-3f41-9c17-57b7a7d74293 | -9.302 | -47.0542 | 2025-10-30 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 599c9345-e72e-3f9f-b5b7-7cafdc65efda | -6.7129 | -38.1913 | 2025-10-30 14:20:00 | GOES-19 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 59066fef-c4f6-3597-9b7e-340b7e8de01e | -10.4871 | -45.0387 | 2025-10-30 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| cc367ac7-ed0a-3477-8bad-0b70483267ff | -9.8437 | -44.8679 | 2025-10-30 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 9dc1c3f7-3f31-376d-8172-2300f2fe1ef9 | -6.157 | -42.3868 | 2025-10-30 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| ea91249f-2dc6-3a9d-8f13-d69dbb81c08f | -9.2653 | -45.5762 | 2025-10-30 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 75835199-b9a3-33bc-b513-974f1e7cdfde | -10.266 | -44.5835 | 2025-10-30 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 1cb47f4d-7f70-3910-8cdf-4295e8565bd0 | -8.0636 | -45.1359 | 2025-10-30 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c4118407-92f3-39ae-b0a4-59e5e9e837a3 | -13.5876 | -47.3438 | 2025-10-30 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 53596fe2-864a-3bef-944b-f0600a70f3a5 | -7.9215 | -46.0094 | 2025-10-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |


[Clique aqui para ver as próximas entradas](README70.md)
