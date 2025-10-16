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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 556a9e6f-6e3d-31c0-aef6-3e97ff7a718c | 1.84 | -55.7626 | 2025-10-16 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0d6afe77-317a-3ef7-9139-663645ae2bf5 | -4.3498 | -43.4082 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 27ad7051-1e2a-342b-8490-9f7f23ce04b6 | -4.3874 | -43.3827 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 304.5 |
| 6f19a576-04e2-3024-b975-f45de48b4073 | -5.4375 | -40.9826 | 2025-10-16 02:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 53d989c4-3e4f-3a6b-b798-7b12f9c9c898 | -4.0976 | -48.0144 | 2025-10-16 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 134adec3-a086-342e-b077-5fe263e28c17 | -4.6624 | -44.1062 | 2025-10-16 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e70b8daa-b2b6-314a-b5f0-5ebb41239623 | -5.4575 | -42.9381 | 2025-10-16 02:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 597fddfd-47ff-33c9-b304-418b486e280e | -4.3872 | -43.406 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 373.3 |
| 1ef3b783-bbe3-34b5-a14c-427e8d0c8646 | -8.4528 | -44.1767 | 2025-10-16 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 650da048-db4f-3148-b372-8bc0b100e413 | 1.8217 | -55.7629 | 2025-10-16 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5cb9c9aa-7828-347e-8a1e-661ffcc67cab | 1.8218 | -55.7431 | 2025-10-16 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f1d8414b-3c23-394f-a2a9-978e6a283fbe | -5.4764 | -42.9132 | 2025-10-16 02:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 8c5ffa8e-a2e4-3825-b25e-98d523fcea11 | -6.0487 | -41.9437 | 2025-10-16 02:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 7341fb1a-263c-31eb-94c3-ff84c0fba82d | -4.1161 | -48.0136 | 2025-10-16 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 67c8e858-d871-376b-b032-3816b2d10901 | -4.4059 | -43.4049 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b1f57762-ea2c-3fd0-8421-b3657119aa3b | -8.4717 | -44.1746 | 2025-10-16 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ea141eb5-ee55-3225-a637-aaad55172934 | -7.9628 | -44.1362 | 2025-10-16 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e151d7a3-7176-34cd-8ac3-9d2a0ba68f00 | -2.9972 | -45.3685 | 2025-10-16 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 883a5d31-b239-345b-9e1e-61c91f12f751 | -3.0343 | -45.3896 | 2025-10-16 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| f717c82a-9b37-3f94-aafa-c66826ebc5b4 | -3.0158 | -45.3679 | 2025-10-16 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 3e5017f8-8cd1-36ec-8f19-e48d1539401f | -4.116 | -48.0352 | 2025-10-16 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| eec65bd6-a749-381c-bd81-dd46d024f455 | -4.8644 | -44.5748 | 2025-10-16 02:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6a825a0b-9866-312a-bb85-5d9a54e84a59 | -5.4762 | -42.9367 | 2025-10-16 02:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| e1df4eb1-f705-381f-8a2c-c07f2942cfea | 1.8401 | -55.7429 | 2025-10-16 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e6f46ef0-f615-386c-aca6-7d7ee6e46d5f | -2.9971 | -45.391 | 2025-10-16 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9c78390f-2ebd-34f9-98b0-d73007422a0c | -4.4061 | -43.3816 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| cb778a6f-cd3e-3d87-b149-b7d0189eb3ca | -4.3687 | -43.3838 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 361.0 |
| 9e5e5aba-524b-3a9c-931d-150b7f2771ff | -5.5147 | -47.3069 | 2025-10-16 02:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f3678d90-22de-3fb0-b521-fc292f6a73d8 | -7.9439 | -44.1381 | 2025-10-16 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c94c361e-c156-304e-bc36-8508198635b4 | -8.4714 | -44.1978 | 2025-10-16 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 04838197-d71a-3e3c-8a63-b7ca7e5731a3 | -4.6626 | -44.0832 | 2025-10-16 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 3f26af6d-035f-3a16-bbed-6a53c013b2d8 | -10.133 | -44.5777 | 2025-10-16 02:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 127.1 |
| bc7b6b3e-c3fe-3701-9e47-32773d1a70b4 | -4.0974 | -48.0361 | 2025-10-16 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| b646546a-1bce-31a8-a4ed-2a383d10f23a | -12.6805 | -43.4235 | 2025-10-16 02:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 22f3ae7d-473a-35b6-be83-e354ed4041a7 | -5.5147 | -47.3069 | 2025-10-16 02:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ae676fc6-ee14-3f0e-8d06-82fc985f92c0 | -4.5041 | -45.4118 | 2025-10-16 02:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d764107e-7454-3fdc-9f05-465bf96f924e | -5.496 | -47.308 | 2025-10-16 02:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 18aff5e9-e885-30df-bf77-336907a4ac75 | -5.4575 | -42.9381 | 2025-10-16 02:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| cfec72d3-b24f-3d3c-8a6b-05da0c8fb42e | -5.4764 | -42.9132 | 2025-10-16 02:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 194e37d1-7711-3a65-904f-74a3be71c3d5 | -6.0487 | -41.9437 | 2025-10-16 02:40:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 59.1 |
| ee9860d4-1efc-3764-a472-c152685ab9e0 | -12.6805 | -43.4235 | 2025-10-16 02:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 0fe1cd06-964a-318a-bf08-b85a42c9f208 | -4.6626 | -44.0832 | 2025-10-16 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3e102e17-f362-3797-8cd1-ea7ec876ae00 | 1.8401 | -55.7429 | 2025-10-16 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f54de90d-cbbe-37ca-baf9-f90d7ebc3e95 | -5.8799 | -43.8844 | 2025-10-16 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 51965f8b-9885-3517-9e8e-87e555abaf6f | -4.3687 | -43.3838 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 284.8 |
| 4c855805-e654-38ac-82af-50e3613bc564 | 1.8401 | -55.7232 | 2025-10-16 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 5ebcbd10-f5ee-305b-94d5-3014ba912756 | -4.0974 | -48.0361 | 2025-10-16 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 417b133a-5c0c-3af4-9bd6-1a83fb723d0c | -4.0976 | -48.0144 | 2025-10-16 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 816a210a-13cc-38a0-ab40-2e159787fc7d | -3.0157 | -45.3903 | 2025-10-16 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 180.3 |
| f45aba08-2d7f-3c5b-bb1d-85809744560c | -3.0158 | -45.3679 | 2025-10-16 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8d62122d-0151-3dcc-b9da-5f3ca25abc2e | -4.3685 | -43.4071 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 258.5 |
| caacd764-2265-3459-9f5f-78ac636c0ec1 | -10.1333 | -44.5545 | 2025-10-16 02:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 56107890-46a0-3370-905b-bcbbd8ab9841 | -6.1723 | -40.8954 | 2025-10-16 02:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 23a88645-a45f-34f7-b5da-de15d7c14818 | 1.8217 | -55.7629 | 2025-10-16 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 86be2723-c18a-3eb6-97cf-1c01a98af021 | -4.3872 | -43.406 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 347.2 |
| 63c1f3f2-ab78-33fa-a709-e5e962ce7ce6 | -10.133 | -44.5777 | 2025-10-16 02:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 177c6560-7b9e-3650-af4f-f52ee2eab63a | -5.4762 | -42.9367 | 2025-10-16 02:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 180.0 |
| 333d9d70-ca9b-3d9a-bc07-67a234972d2c | -5.6821 | -45.0893 | 2025-10-16 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| ce48204b-3e52-38dc-b2be-05d3dba13915 | -8.4717 | -44.1746 | 2025-10-16 02:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 440f186f-5e3c-3e46-afb5-283414f36e93 | -7.4706 | -42.7605 | 2025-10-16 02:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 555a156d-0155-3bae-a6c6-e79a433632b5 | -10.1326 | -44.6008 | 2025-10-16 02:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1529924d-4b97-3b64-97fb-436ef29eff4e | 1.8218 | -55.7431 | 2025-10-16 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6a63a597-f3fc-35e4-9cd9-800be025b11b | 1.84 | -55.7626 | 2025-10-16 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f296cb0e-8bdb-3c0a-bd5f-1087cc20aece | -4.3498 | -43.4082 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 87588e00-cfe6-3049-a726-4e23d53352ce | -4.3874 | -43.3827 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 350.2 |
| 6f2e5687-8357-3696-9305-4f4448a7ece9 | -7.9439 | -44.1381 | 2025-10-16 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cee17677-bed7-351b-85b3-52f72a3f452c | -4.4059 | -43.4049 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c5d81663-5fcd-3c09-a2a8-815be523ba90 | -5.4276 | -44.2402 | 2025-10-16 02:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 7f7420c4-840c-3da4-ac2a-6546716c57ba | -4.1161 | -48.0136 | 2025-10-16 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 5202005b-32aa-32cc-8bb7-d91e9d308d15 | -7.9628 | -44.1362 | 2025-10-16 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 24af4deb-a524-3cd5-8a26-2058a9175b44 | -4.35 | -43.3849 | 2025-10-16 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 88a0da09-8306-38da-80b8-b6542529d1d3 | -2.9971 | -45.391 | 2025-10-16 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 959a0ae5-98ff-3e3e-8841-b6927471f9c9 | -3.0343 | -45.3896 | 2025-10-16 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 106d3102-48e5-3cb3-87d1-c2934b770b00 | -4.116 | -48.0352 | 2025-10-16 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 584b549d-08d7-363b-ac84-297f4fa8388e | -6.1534 | -40.8971 | 2025-10-16 02:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| c4cc15b5-d1ab-3fbd-ab29-b3a7874d3570 | -4.6624 | -44.1062 | 2025-10-16 02:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| ad5bfd79-8875-3edb-9ebc-0be30dabc3d0 | 1.8401 | -55.7232 | 2025-10-16 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a7986b57-3b80-3d93-9984-556889cc6091 | -4.4059 | -43.4049 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 77e7d1a8-03ce-3870-90f8-06b6fe541bc4 | -2.9972 | -45.3685 | 2025-10-16 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| da92f8d9-d42e-346b-b5b9-0e670827a06c | -4.3874 | -43.3827 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 275.3 |
| 12200cc5-dd80-3f73-99de-eb59a586dbbf | -4.116 | -48.0352 | 2025-10-16 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 664574b5-cde6-30f7-8843-289e65027c0f | 1.8217 | -55.7629 | 2025-10-16 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9727449e-68e2-307b-bd27-de3a8173e3cf | 1.8218 | -55.7431 | 2025-10-16 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| aa81a7fd-9668-37b3-b539-49f7de863a5b | -8.4717 | -44.1746 | 2025-10-16 02:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ad68cd54-51ef-340f-aa45-79ae45d85048 | -5.496 | -47.308 | 2025-10-16 02:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| cf324044-60ee-36a3-999b-76cbd2d9b5c2 | -4.3687 | -43.3838 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 9616d368-6cf3-3ed5-8556-31ab5bfe63ad | 1.84 | -55.7626 | 2025-10-16 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 59935d8b-84dd-308e-859b-ca6130f48a0d | -2.9971 | -45.391 | 2025-10-16 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| db7c929d-1d18-3022-a504-efc6b8d1907e | -4.3872 | -43.406 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 3fdc6fbc-dd18-32e6-953c-6b05cd85206d | -5.8799 | -43.8844 | 2025-10-16 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 71e346bf-2c93-3107-a4ef-0eae0401d304 | -2.8829 | -50.7356 | 2025-10-16 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ac6d25cf-bdbc-3c9c-a0ac-1755b112d1ca | -7.9439 | -44.1381 | 2025-10-16 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b883dc5d-6277-3a9b-8d66-b0c6abc9428f | -4.6624 | -44.1062 | 2025-10-16 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d609c625-dbe6-38ef-96cf-63588a868e00 | -4.6626 | -44.0832 | 2025-10-16 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b0df204e-f9f0-3eae-8c9b-b029f2c7eaf8 | -5.4764 | -42.9132 | 2025-10-16 02:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| f223689a-8b6d-385a-be80-fa268c5d138c | -4.35 | -43.3849 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 41df0c52-897d-3d24-9bef-0f6ce351e5bc | -6.1534 | -40.8971 | 2025-10-16 02:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| e50a0628-a3e3-3917-872f-eb0be2146af1 | -4.0974 | -48.0361 | 2025-10-16 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| c630a85a-520a-303e-ba19-d97c16aa50b0 | -4.3685 | -43.4071 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 5185b294-2a10-303e-9345-693b149a6aa8 | -10.133 | -44.5777 | 2025-10-16 02:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |


[Clique aqui para ver as próximas entradas](README10.md)
