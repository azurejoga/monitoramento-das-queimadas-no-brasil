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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c55a0a1f-ea0f-38be-a999-c5656c379532 | -3.1972 | -50.5592 | 2026-10-08 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 74be1b1b-a80c-3c92-97fa-f3fdca7d32b7 | -3.5515 | -59.4807 | 2026-10-08 03:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 293c96c4-963b-37f0-8699-dcb1eac08cb9 | -7.0065 | -59.1223 | 2026-10-08 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4c39543d-737f-303f-96db-39e97ed31170 | -1.5306 | -54.5558 | 2026-10-08 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 779d07fa-3d5a-3416-8bd5-b30e09ed33fe | -5.6932 | -53.487 | 2026-10-08 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 6ff722ad-0cba-3143-ad6f-567926c89944 | -2.7797 | -54.0736 | 2026-10-08 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b14888d4-4ff3-3b9a-9955-9d0b69adffb3 | -4.3471 | -43.8021 | 2026-10-08 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 054e43f4-f463-3415-adce-e330ee242b84 | -3.1101 | -54.1661 | 2026-10-08 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1e68a8c6-3170-328b-be87-5552e5c809f5 | -3.1601 | -50.6021 | 2026-10-08 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a5b3bb51-3398-304e-a6d0-cecbabcd2bd4 | -3.11 | -54.1862 | 2026-10-08 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 622fb7ad-9551-37d2-ab67-6f38fe7204a2 | -9.475 | -64.3525 | 2026-10-08 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5e69e57b-e462-3d73-8433-cc29bc53985b | -3.0913 | -54.287 | 2026-10-08 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 84c2ecfa-1168-3b12-8ef0-d02f942d8d4d | -3.0925 | -53.9455 | 2026-10-08 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2c67635b-c43d-3a5c-b385-d72a18c348b3 | -2.572 | -56.1646 | 2026-10-08 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f4783e0c-cbbc-3b95-88fc-8b65295747c4 | -8.742 | -45.1563 | 2026-10-08 03:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 7b160012-d569-317b-9a74-097261ec7e46 | -11.6365 | -43.7113 | 2026-10-08 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| c5896fa1-ccd2-3332-8daa-291f960ca463 | -2.7796 | -54.0937 | 2026-10-08 03:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c45d9757-5e3f-3990-8399-d1d78d8297ef | -3.0741 | -53.946 | 2026-10-08 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 6527603f-6ad6-3762-8dbb-4e4d17088db4 | -2.499 | -56.0675 | 2026-10-08 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2bd33875-b254-320a-9253-02733d51474d | -2.7152 | -57.472 | 2026-10-08 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 8aa33700-154b-3aac-aa04-640e5e77bf1e | -2.4805 | -56.1269 | 2026-10-08 03:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5d39cfd7-37ee-3932-91d2-f289d0d21d2b | -3.1114 | -53.7839 | 2026-10-08 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4ccd5748-d19b-3d5d-bcaf-0c4aebdad0b0 | -10.4337 | -47.2824 | 2026-10-08 03:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| cc105679-f500-35b0-ba80-86f29615fef4 | -2.9448 | -54.1501 | 2026-10-08 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 819104c4-a21b-326d-89c5-a3ad308ecbb2 | -11.6369 | -43.6876 | 2026-10-08 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 569a27a9-4212-367e-80c1-25b8e879f587 | -3.0 | -54.11 | 2026-10-08 03:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e649cd76-3533-3e61-bf73-38927309ac02 | -6.67 | -43.75 | 2026-10-08 03:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d5981b0-d587-39a8-80bb-028f5ff5d760 | -6.64 | -43.7 | 2026-10-08 03:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b7273cc-c96b-3a85-b48a-67960fff4ace | -3.02 | -54.11 | 2026-10-08 03:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2d26da-dd81-3898-8568-b53e9c8b9730 | -6.61 | -43.74 | 2026-10-08 03:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 057bd613-13ce-3107-a2f3-74f882ce6746 | -8.73 | -45.15 | 2026-10-08 03:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94c00e03-eb0b-3dd8-bee4-ef998aceb666 | -6.64 | -43.75 | 2026-10-08 03:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca8f5fe-fe1a-3706-90f6-b43b0e4a47b8 | -3.0 | -54.04 | 2026-10-08 03:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a84982-eb0b-3dc2-8865-1e9f3c5809b0 | -3.074 | -53.9661 | 2026-10-08 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a90f82f1-1272-33d3-bff5-a49114596d54 | -2.4032 | -57.8848 | 2026-10-08 03:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 5f83db3d-b1f1-3485-9a13-ab0ddada1f15 | -4.3471 | -43.8021 | 2026-10-08 03:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0f025107-5f5a-35af-8931-28f426fe05dc | -3.073 | -54.2874 | 2026-10-08 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 05292f39-6af9-343c-a29d-a8001fdd2be0 | -7.0065 | -59.1223 | 2026-10-08 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 96bb7bdf-d8ba-3914-88b6-c7d23f08ea71 | -3.11 | -54.1862 | 2026-10-08 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 66a0bd07-20bc-3738-8292-6a406e0ac881 | -6.1431 | -47.9214 | 2026-10-08 03:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 96a16f40-b0af-373d-98fa-20a01056d32e | -2.4031 | -57.9041 | 2026-10-08 03:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e08b38cf-2099-3831-a058-5e134e2f54f9 | -3.1101 | -54.1661 | 2026-10-08 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 81a87d35-931e-3da9-b31f-e63875f02d8d | -2.4805 | -56.1269 | 2026-10-08 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 75ac7480-bce0-3049-881b-4dfd384a853b | -3.1114 | -53.7839 | 2026-10-08 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5df487de-0741-3052-97b3-f02461331ba8 | -8.7228 | -45.1812 | 2026-10-08 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| be70bc1c-561f-3943-ae63-777d24f50829 | -3.0925 | -53.9455 | 2026-10-08 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 60b73f44-1f63-31a7-a67f-0735f14b09ad | -2.572 | -56.1646 | 2026-10-08 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2ab365fc-ca19-3ebc-8cbd-6ebf3cb61e91 | -5.7117 | -53.4862 | 2026-10-08 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 920d7abd-fa81-3a44-99dd-aa04b5939fe5 | -3.1601 | -50.6021 | 2026-10-08 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 690dcede-ab0d-357f-b6f8-29e83fe2bb91 | -11.6369 | -43.6876 | 2026-10-08 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 52f95166-93b0-3e79-ae0f-30f9f85c7115 | -9.0592 | -65.9209 | 2026-10-08 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 058c8b2e-1509-314f-a067-1f044a4acb30 | -3.0741 | -53.946 | 2026-10-08 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| a6f2ae95-784e-3816-b575-f5ed514e1423 | -2.4987 | -56.1659 | 2026-10-08 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0d57bcb1-2a2a-3b80-bfd5-ac604d0085a9 | -1.5306 | -54.5558 | 2026-10-08 03:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f1ea8987-9334-3082-9f83-efda78d1fae4 | -5.7376 | -45.1533 | 2026-10-08 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4f0f8c33-269e-355a-88b5-f94dc3303af8 | -2.4988 | -56.1462 | 2026-10-08 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| cc222beb-a684-3252-8e44-acd0d5c0b82a | -2.7797 | -54.0736 | 2026-10-08 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d2852197-1178-3d57-9d78-9fb65c106de9 | -2.499 | -56.0675 | 2026-10-08 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2497c12a-736c-3055-aa8f-3a890aa76239 | -3.5865 | -54.5742 | 2026-10-08 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 285fd276-5a39-3e25-ac5a-bb12cc87e162 | -3.1285 | -54.1657 | 2026-10-08 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| c6fa94f9-dea3-3a4d-8f8f-f5a3bef37a98 | -2.7152 | -57.472 | 2026-10-08 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1b942b07-3032-31b2-86ae-4bf0f8b53c52 | -5.6931 | -53.5073 | 2026-10-08 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cba86e27-ed13-34b6-b15f-f175f44f790c | -9.475 | -64.3525 | 2026-10-08 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 5da997dc-e888-3ce5-a992-81e31e6c00f8 | -6.1429 | -47.9432 | 2026-10-08 03:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6f9fab84-36f2-3a7c-a5e9-d873a732f5d7 | -3.1972 | -50.5592 | 2026-10-08 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 53028a9e-3a09-3e24-a24a-bfb2778ed10f | -8.742 | -45.1563 | 2026-10-08 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 519e66ad-c35a-37f6-919f-0da2b11bae49 | -5.6932 | -53.487 | 2026-10-08 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 9b9862ad-3521-3d74-b9ac-1c8d1638e556 | -8.7231 | -45.1583 | 2026-10-08 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 6f024aac-28a1-321b-8b56-6bc3c7970541 | -2.7335 | -57.4717 | 2026-10-08 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 04a43d6d-1faa-3da9-bde6-8194490ea2b6 | -2.7796 | -54.0937 | 2026-10-08 03:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 88d9b948-f847-3395-a81a-b97f67c38866 | -3.0913 | -54.287 | 2026-10-08 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2d257611-efdf-3ab8-a74f-290561928516 | -2.4805 | -56.1072 | 2026-10-08 03:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| fd0820e0-d41a-3aa3-82c0-63539035fd09 | -1.5306 | -54.5558 | 2026-10-08 03:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 7eb5df6e-1d40-3f77-a460-767d2ba0dadb | -7.0065 | -59.1223 | 2026-10-08 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| e5f49710-e992-381b-9e80-82193eac0a0a | -6.1617 | -47.9201 | 2026-10-08 03:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 686f131b-95e2-386d-8207-c64713ada9d0 | -8.7231 | -45.1583 | 2026-10-08 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 27688afd-af1a-3288-8c54-db6dca577b61 | -3.5493 | -54.6752 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7dfec206-9237-3d13-85b7-5fd68f4e8c0c | -9.475 | -64.3525 | 2026-10-08 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d348e925-22f2-30c8-925b-4eb1c37fc895 | -6.6315 | -43.7533 | 2026-10-08 03:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| a41872b3-f6da-3147-a622-96b6c4a42772 | -6.1429 | -47.9432 | 2026-10-08 03:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6b07214d-cab6-3cf7-960e-4f80278be708 | -3.0925 | -53.9455 | 2026-10-08 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 531a0339-1b51-37a2-8958-e202dd84cb13 | -3.074 | -53.9661 | 2026-10-08 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 29f92cfa-8214-31d7-a8e8-d1637b50a61a | -3.5677 | -54.6746 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| e4e9417b-699a-3662-961d-f4d7203bbe2d | -6.6317 | -43.73 | 2026-10-08 03:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 9a79a6ee-4bd2-3950-b174-2703cb023719 | -2.4805 | -56.1269 | 2026-10-08 03:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| fa9f68d9-cb94-3803-9674-ecb20a0cb4fd | -6.1431 | -47.9214 | 2026-10-08 03:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| d90116c7-b09a-3930-8018-8b8b538fb71d | -5.7376 | -45.1533 | 2026-10-08 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 09c71734-81b8-3b39-bb82-c40c61291bc1 | -2.7797 | -54.0736 | 2026-10-08 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 84c94987-6885-3ea8-b6c5-43381f18cfe8 | -2.499 | -56.0675 | 2026-10-08 03:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2e9a61b3-e38a-32e9-b6b5-f2e6d2403d7f | -3.11 | -54.1862 | 2026-10-08 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 204175c4-a3f7-32f4-a6af-a07f505e6ea2 | -3.1972 | -50.5592 | 2026-10-08 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| b33ab4f8-6a86-3005-8fc8-51be207d6655 | -2.7335 | -57.4717 | 2026-10-08 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9bce6493-d1f8-32e3-8e7f-7ec2ab3a7474 | -3.0913 | -54.287 | 2026-10-08 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1e22832e-9e58-3da0-ae05-541783f9a903 | -8.7228 | -45.1812 | 2026-10-08 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 49933cba-e737-3096-99cf-88424f9651c2 | -6.6505 | -43.7284 | 2026-10-08 03:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 66d9ca8a-8b33-32e6-a4a1-cc2048b3552e | -7.4443 | -63.5401 | 2026-10-08 03:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 46a9861a-64f5-3fe1-82b6-e8bd6b5225ad | -8.742 | -45.1563 | 2026-10-08 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| fa903e27-2cc3-3c29-aec4-31d36961f4ff | -3.5865 | -54.5742 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d9ae4c19-729d-3f01-9324-4977e6c29d94 | -3.0741 | -53.946 | 2026-10-08 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 41f77591-bd89-303e-baed-d908e846903c | -8.6107 | -67.0301 | 2026-10-08 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |


[Clique aqui para ver as próximas entradas](README55.md)
