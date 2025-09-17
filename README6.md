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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c016e9f2-53d1-3036-a2d9-f399835f40bf | -4.0634 | -47.4943 | 2025-09-17 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 5b429470-14f6-38d5-9f92-64859ad1af0f | -6.6127 | -45.6066 | 2025-09-17 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1f3f1772-7d0f-3d04-866b-3654ae5e3a0d | -7.581 | -44.566 | 2025-09-17 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 06fdf8c2-caa1-3949-a9b7-3cae59ee1f68 | -6.6808 | -46.2961 | 2025-09-17 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 189.4 |
| ea3ebdfe-6753-3613-86d8-4e031c947abf | -11.0201 | -45.059 | 2025-09-17 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c383244b-2ddc-3670-9d6f-97d81ed521ba | -7.5807 | -44.589 | 2025-09-17 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| a2c76737-3dc3-3e02-ad4d-4296750b592b | -6.6314 | -45.6051 | 2025-09-17 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 964fdd1b-28d7-3c4e-bac7-5dd03c27be84 | -15.3996 | -46.1477 | 2025-09-17 00:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 180.8 |
| f6666c2e-1747-3742-8572-d32d32fe2579 | -11.0164 | -48.9297 | 2025-09-17 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| ceb419cc-20be-3392-a34b-8fecd5c7cdcc | -7.5807 | -44.589 | 2025-09-17 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.3 |
| a0ac52fb-9515-32fd-b88f-e70704290884 | -6.8922 | -43.9619 | 2025-09-17 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 94cad4fb-4fe5-3f83-8565-4b3db317a19a | -4.0634 | -47.4943 | 2025-09-17 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| a0ff8b23-d720-3fc4-ac52-61e64a312375 | -10.6541 | -46.5177 | 2025-09-17 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 4274319d-72eb-38fd-813e-681867f74d6d | -7.5996 | -44.5872 | 2025-09-17 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 781e4c35-0744-3952-b158-a67659e839e5 | -11.0167 | -48.9079 | 2025-09-17 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 48babd29-c4ef-3ae2-b969-858be1a03ee4 | -6.6806 | -46.3184 | 2025-09-17 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a265f273-fd9e-3f0b-817a-25a670023de7 | -19.4927 | -43.444 | 2025-09-17 00:40:00 | GOES-19 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 017219eb-22d8-3169-9d0b-418f7223ce02 | -6.6808 | -46.2961 | 2025-09-17 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 911f5af3-4e4c-301d-83a6-331352b4fa1f | -6.6316 | -45.5825 | 2025-09-17 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8b190d5e-ad24-3d0a-848e-7547e6f5624f | -6.8734 | -43.9636 | 2025-09-17 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 03a994e1-1094-36bf-91e8-cfcc44e5aa68 | -7.5998 | -44.5642 | 2025-09-17 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 44aa1eda-224d-3833-afad-ee784e545522 | -15.4192 | -46.144 | 2025-09-17 00:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 190.0 |
| dce7644a-880f-3ce0-8784-67b1a53d22fc | -7.5622 | -44.5678 | 2025-09-17 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| caf1f370-20c8-3efb-964e-04f93f4da2a8 | -15.4187 | -46.1672 | 2025-09-17 00:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 644df3ec-7005-3646-af9a-e5a961c9fcc3 | -7.581 | -44.566 | 2025-09-17 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 92c358e1-1c86-3edf-b657-a45edac0539a | -15.3996 | -46.1477 | 2025-09-17 00:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 119.0 |
| ddc68cac-b96b-396f-8796-fa6324ff10df | -4.0633 | -47.5161 | 2025-09-17 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1e0cb9d3-aea8-3b4f-a64a-d8a85b7d73ca | -7.5996 | -44.5872 | 2025-09-17 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 04f23f19-50a5-3c26-8930-3b0bd68e74f6 | -7.2583 | -46.5829 | 2025-09-17 00:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 7b204268-89eb-314e-ba1f-a9d01f2ef8cf | -6.6806 | -46.3184 | 2025-09-17 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d8158d6a-ba9f-398c-8748-91980c07b945 | -7.581 | -44.566 | 2025-09-17 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 5616576e-c0f8-39c9-87ab-9447262aff9c | -15.4192 | -46.144 | 2025-09-17 00:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 1c248dcc-75b0-31b1-b6e8-0406bf4b4f0f | -6.6808 | -46.2961 | 2025-09-17 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 5a76af71-df2f-37cc-8892-9829c9ee11ce | -11.0164 | -48.9297 | 2025-09-17 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| eb639a45-cf5e-39c1-8584-4885c52c6c60 | -7.5807 | -44.589 | 2025-09-17 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e2a1e97d-089e-3978-944d-3e6279dfc779 | -7.8785 | -48.1585 | 2025-09-17 00:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 08ce6193-001a-369e-9190-24c08c715af9 | -20.2011 | -42.2991 | 2025-09-17 00:50:00 | GOES-19 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| 1888149e-4d1f-3793-94f1-bc34bd89fab6 | -6.6129 | -45.584 | 2025-09-17 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| bc6b0bce-696d-3168-b0f0-37853f1a0573 | -4.0634 | -47.4943 | 2025-09-17 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| a220c34c-d09c-3772-8187-2a6ef9f98c15 | -14.8207 | -51.7006 | 2025-09-17 00:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b95f2450-1050-37c9-b45a-1a94b445da58 | -20.1805 | -42.3051 | 2025-09-17 00:50:00 | GOES-19 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| c8bbc1c3-562e-32a1-9a33-e9bb163ba72e | -4.0449 | -47.4951 | 2025-09-17 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f5920779-5a23-3c62-8c48-b4bd499f6da4 | -23.4189 | -47.1695 | 2025-09-17 00:50:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 8744fbb8-f455-3a0e-8bd3-f6c7e8a2503f | -6.8734 | -43.9636 | 2025-09-17 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a8cee1a6-4eca-3438-b597-4110518a028b | -15.3996 | -46.1477 | 2025-09-17 00:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 524b3c30-133b-30a7-b58b-a5d68cf12a66 | -17.0593 | -45.891 | 2025-09-17 01:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e1718ae5-4e91-3fb0-8315-d1b28ad34776 | -6.6808 | -46.2961 | 2025-09-17 01:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 064247a8-3747-39b0-bbb9-5479839ea7fa | -15.3996 | -46.1477 | 2025-09-17 01:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 13847efe-7478-3d38-a3da-16d5ea7ff0b6 | -6.6806 | -46.3184 | 2025-09-17 01:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f6ed4e01-cc07-3886-845c-83238e894b5e | -7.581 | -44.566 | 2025-09-17 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.0 |
| b42a1935-e939-3884-a273-89832646ede8 | -11.0164 | -48.9297 | 2025-09-17 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 56703d8c-8fee-3cae-94c0-ecf8f34a1de4 | -15.4187 | -46.1672 | 2025-09-17 01:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 476e058b-0c24-3b98-87d9-52d0543b59fb | -4.0634 | -47.4943 | 2025-09-17 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 62323305-b3fb-3657-bb9d-8c60a4ce9101 | -4.0633 | -47.5161 | 2025-09-17 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| c8872462-ae50-3979-b29d-c03dc1a5f79d | -15.4192 | -46.144 | 2025-09-17 01:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 837c764f-913c-3f1e-9fb6-8b02b905157b | -7.5807 | -44.589 | 2025-09-17 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 387c8612-fc7f-3d91-9da3-b87b758bdc0d | -8.5445 | -48.9673 | 2025-09-17 01:00:00 | GOES-19 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9f3f7170-c9b8-327e-a791-e95abe69a7aa | -6.8734 | -43.9636 | 2025-09-17 01:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9f074712-03a3-3f2a-b8fe-012ff7b352c1 | -8.5445 | -48.9673 | 2025-09-17 01:10:00 | GOES-19 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7aa3ca52-751f-3b42-9753-28864d123577 | -15.4187 | -46.1672 | 2025-09-17 01:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 22355722-34ec-3924-9211-a38a2e0ab92e | -17.0593 | -45.891 | 2025-09-17 01:10:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 18fb2523-7d84-3c83-ab7d-548c50ea01f6 | -7.8783 | -48.1803 | 2025-09-17 01:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fa391875-6980-3d81-a8df-cfd9f8184569 | -6.6806 | -46.3184 | 2025-09-17 01:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7f1f670c-846b-3093-a4b8-0615e35e617c | -6.6808 | -46.2961 | 2025-09-17 01:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| f5a25af3-7fa1-38f8-9f38-8d297ccf05c6 | -15.4192 | -46.144 | 2025-09-17 01:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 137.0 |
| cffcfc95-aa7a-3aa4-bce7-2ba05f1f36b2 | -7.581 | -44.566 | 2025-09-17 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 3d528673-3126-3dac-9ee8-9155da7d02ef | -7.2583 | -46.5829 | 2025-09-17 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c4584318-94ea-3e88-a55e-bfa8782a2178 | -7.5996 | -44.5872 | 2025-09-17 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 266ce9d8-13a2-3397-b521-3edf747c3b0a | -15.3996 | -46.1477 | 2025-09-17 01:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 0d4a8d36-0cc8-3889-b3b3-fcaab7bd3323 | -7.5807 | -44.589 | 2025-09-17 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5758a4dc-3bee-3b0f-98f5-a90ec41a72d1 | -6.8734 | -43.9636 | 2025-09-17 01:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 425b1ef6-c00b-306c-9cc7-bc52525e28d7 | -2.3763 | -47.6419 | 2025-09-17 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1a70b5aa-2352-39f5-86ea-581ae18e9588 | -4.0633 | -47.5161 | 2025-09-17 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1e7cda4d-ab5e-3801-9b0a-5f46b0b75bce | -11.0164 | -48.9297 | 2025-09-17 01:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 478273ba-f718-39d5-9d0d-71323fc1679b | -4.0634 | -47.4943 | 2025-09-17 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 5df8dc96-bb6c-3344-b2c4-33ff97eb9d7b | -4.0449 | -47.4951 | 2025-09-17 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f9ade643-3c49-3bad-8930-ac638219c6c9 | -15.3996 | -46.1477 | 2025-09-17 01:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0be51777-f4dc-3a23-bf09-95f92e1ce10c | -6.6808 | -46.2961 | 2025-09-17 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| b73bf61d-4908-3736-8a3d-5524816424a7 | -7.581 | -44.566 | 2025-09-17 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| cb96ea7f-9336-301c-875d-81115b8ee41a | -4.0634 | -47.4943 | 2025-09-17 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 33d07646-cdd0-3df6-aab5-d6504d17c23b | -6.6806 | -46.3184 | 2025-09-17 01:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 90a5d051-bbb2-302f-a8cc-058269e12dff | -4.0633 | -47.5161 | 2025-09-17 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8f30c8c7-dad6-3120-9c41-316a1a85a57c | -4.0449 | -47.4951 | 2025-09-17 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 53fc4717-8a6f-3a27-a4f9-e6620fb0c0f4 | -7.5807 | -44.589 | 2025-09-17 01:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c50da6c0-9390-3127-b0b7-fb0791c8de34 | -11.0164 | -48.9297 | 2025-09-17 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0898d0f9-cffa-3403-b8c0-4aed9586713b | -15.4192 | -46.144 | 2025-09-17 01:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| de4507a2-c0d0-3d39-9b49-c645ea49d949 | -7.5807 | -44.589 | 2025-09-17 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 09fbe86d-2096-3b66-b4b7-5f5211cca63b | -15.4192 | -46.144 | 2025-09-17 01:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 87f09418-e64a-39e4-97f4-69a7367013a9 | -14.9177 | -51.6872 | 2025-09-17 01:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 92254cd2-6cdc-3518-95d3-e0aa7e7ce69d | -14.9371 | -51.6845 | 2025-09-17 01:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 6095dfdd-9116-3318-b382-d3476c1f08ed | -4.0634 | -47.4943 | 2025-09-17 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| b4a4fc7f-4530-328c-8c3e-8c88383bfffe | -10.8017 | -50.7178 | 2025-09-17 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 7a3f0a4b-af8b-3161-8dec-8303f2a37e49 | -10.7827 | -50.7198 | 2025-09-17 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1c58f006-a2a4-3afe-bf66-a811104e7a0a | -4.0449 | -47.4951 | 2025-09-17 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| dcd87ac3-8a83-3065-897c-defbaeb6029d | -9.1715 | -46.9346 | 2025-09-17 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 85b0b0e7-1792-3beb-9e01-63bb510340cf | -4.0633 | -47.5161 | 2025-09-17 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 15ac742f-600e-36b3-9aca-9dc17b850571 | -15.3996 | -46.1477 | 2025-09-17 01:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 13512d9b-9969-366e-a567-7b588dff1ce4 | -14.9375 | -51.663 | 2025-09-17 01:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 9ca7b37c-337a-36af-befd-d7140f404098 | -11.0164 | -48.9297 | 2025-09-17 01:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ac9f0c26-88f7-38c2-be1a-36ad859305ff | -6.6808 | -46.2961 | 2025-09-17 01:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |


[Clique aqui para ver as próximas entradas](README7.md)
