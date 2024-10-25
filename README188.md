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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ffdfa05-1a80-3e56-ab82-fccea519f7f8 | -2.16384 | -56.21548 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 36db08d6-b654-3399-9916-145267a14058 | -2.93465 | -56.62951 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f3b82380-4d06-3ae9-b757-969fa90b6f08 | -2.93411 | -56.62582 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8e807426-b655-3f1b-b1fc-9090b5ecb0af | -2.87322 | -56.52343 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3e8ec672-c8a5-3347-9049-c51f56f1ad89 | -2.23965 | -56.79702 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5c8e5c8-98f9-3293-932a-bf5afd4236d1 | -2.00453 | -56.56601 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 204.5 |
| ba2abb74-9d83-3913-a900-c2f32ed9f181 | -1.9962 | -56.92739 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 37051b00-f808-3ad1-9ef4-421793adefe7 | -1.99039 | -56.91673 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d4756346-e3e0-37b1-a8c4-3cb03aacf7c6 | -1.98801 | -56.91765 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 08bb5b75-0197-30ea-9535-ba07e08893af | -1.98626 | -56.91736 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 35b026a8-a330-3d21-9a65-14cd36355af2 | -1.97826 | -56.69409 | 2024-10-25 16:54:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4a238a5b-85a6-3a7e-9869-9f99fe50d163 | -1.92575 | -57.03803 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da2a4990-d072-3f55-85a6-ea9a77a13cf3 | -1.86777 | -56.56882 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3b68bac7-1a34-3134-9b3e-36919c55d7af | -2.7771 | -56.99986 | 2024-10-25 16:54:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c71154b-6be8-3f40-86b6-80a7112b2210 | -2.73193 | -57.45684 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a8fe2161-111d-3fb0-899a-086d3e52193b | -2.72637 | -57.44917 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3eb9ef57-eb0e-3b58-a1f7-d24cc8ea6694 | -2.67375 | -57.96889 | 2024-10-25 16:54:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 36646faf-e440-3982-b3d9-7c604de33deb | -2.67005 | -57.35216 | 2024-10-25 16:54:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dac62049-1e05-3d1f-b10a-d1c436b75789 | -2.66943 | -57.34809 | 2024-10-25 16:54:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b3e11d14-56f5-30a4-92d1-f0b19370c57c | -2.66926 | -57.96952 | 2024-10-25 16:54:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2c19655e-2190-3fbc-af50-30507dcd6eea | -2.66087 | -57.14885 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f069829c-ab92-3696-80ad-5405242d9a95 | -2.66027 | -57.14491 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a18df9b-da8c-3d7b-9bce-7ce28b9b5437 | -2.63344 | -57.7944 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0d98c3a6-c193-35ff-bc57-47687fd7767a | -2.6192 | -57.10269 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b67acf1e-fc69-3c40-ac08-0de8426c97a2 | -2.60902 | -57.57521 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a4be6903-6706-310b-95a4-c9d323634c84 | -2.60605 | -57.07269 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a59e64d-5e9b-3cda-8119-455ecd2c2212 | -2.60401 | -57.57166 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 356e7df5-882b-3f22-9587-e43df259424d | -2.59103 | -57.81383 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e096c642-feb6-34f4-bd66-2c7ae181b8ee | -2.58844 | -57.79642 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7516bb09-4cff-3a6f-a1a2-e6c779263f08 | -2.58723 | -57.20798 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a351dfe5-35cd-3d4a-8e55-87f6e0e209de | -2.5833 | -57.15197 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49a81573-fd03-3474-960d-404f016f4491 | -2.56808 | -57.75069 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 052f4936-8f51-381a-850d-0284e0c592d8 | -2.56321 | -57.19046 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 326de1ba-f633-3e15-8292-5e56068b8562 | -2.56261 | -57.18651 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b61f0144-12fd-3d01-981c-462f1d29e171 | -2.55891 | -57.01619 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0c3aace4-3187-3de1-84c4-efc37a36c390 | -2.55834 | -57.01234 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 950afd69-576f-3015-b39c-5ff95f0ad310 | -2.52064 | -56.72889 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4c2a3cda-a33d-3b4f-8348-67bc90aea9ac | -2.51395 | -57.48656 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d6fb78c2-53f1-3b26-bd5e-8557eee6923c | -2.51134 | -57.48707 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 2338af63-bbd6-34ad-a7b7-15497034cc63 | -2.51073 | -57.48293 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| c2b0ff8c-0727-3824-b3f3-bbb7d32121db | -2.50961 | -57.48719 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 402073c1-cdca-3293-8466-87c02ba6ffc7 | -2.50898 | -57.48306 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e2c1b343-3f7d-3fbd-b2b8-1c769b88bb5b | -2.50052 | -57.68985 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5afccab-758b-38a8-913c-c7b7c3185cb4 | -2.48054 | -57.49982 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc0e7986-8f2d-32ea-9447-c01ff5ec7a18 | -2.4681 | -57.47627 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1becf1d6-66b6-3350-9c89-2676c8039065 | -2.46685 | -57.46806 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8f61f027-5168-358e-8c89-a4a5a98cfa88 | -2.45453 | -57.53314 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1919aabc-e545-3fe5-9c76-9e710cb8b315 | -2.44894 | -57.52547 | 2024-10-25 16:54:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23215848-d1db-30b8-8265-b742246b98fb | -2.33763 | -56.9542 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8663e046-129a-36cf-baae-9ffe492d1327 | -2.29102 | -56.88462 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| bbab54d5-60ca-3066-8a88-bd2ff40ab03b | -2.27304 | -56.82257 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| d5d56de5-c1c9-3dd7-a2a6-b8a61862cd3e | -2.26512 | -56.77088 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 641b1b98-97dc-3a83-a2b2-af240919578e | -3.15547 | -58.1363 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 134cf866-275b-31c2-a3b2-2b1c95912a5c | -3.15481 | -58.1354 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a655df54-661f-39bc-86f2-556a09402a23 | -2.98237 | -56.89553 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f0e0948-60c8-3797-9e4a-a3ea34611544 | -2.92885 | -57.54397 | 2024-10-25 16:54:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a8181e85-890f-3bb6-a2f8-809f05c67408 | -2.92384 | -56.99906 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 301fac24-b00f-3ceb-8d88-5c734f8d7675 | -2.92237 | -56.93209 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6f2257e5-814c-3119-9e20-745f78871e4a | -2.91302 | -57.67738 | 2024-10-25 16:54:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 25e6d99c-5e6c-33b0-8651-409529dab4d8 | -2.91092 | -57.39715 | 2024-10-25 16:54:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1c3fa101-3e2c-38d6-ad66-2650b8b2f4eb | -2.88683 | -57.04037 | 2024-10-25 16:54:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a6bb2a0e-d052-33e7-a156-b6a62d751b91 | -2.88122 | -57.43527 | 2024-10-25 16:54:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 08e33dd8-790a-3bc0-b3a7-68f7f5fe3077 | -3.26878 | -58.35918 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 32bcd8cf-dee7-3e4d-9850-a42d6f5d69d9 | -3.26412 | -58.35986 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5a3e14f7-3a62-3a14-a102-d883e164aed3 | -2.99545 | -58.45302 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| c91cb261-df76-3965-84a7-83488e768a89 | -3.41949 | -59.63379 | 2024-10-25 16:54:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e28dd5c4-faa4-3e70-a4aa-55d0022733fb | -3.37425 | -59.80709 | 2024-10-25 16:54:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6205b598-98b5-3735-bba8-5280d5234fdd | -3.20897 | -59.04048 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 2523924e-41ca-3051-bcdb-91c2ac5d4c07 | -3.15795 | -59.83406 | 2024-10-25 16:54:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bd15bb85-67c1-37e3-b1a8-5a6e5e80aebd | -3.14929 | -59.16127 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8c9940fa-e646-3670-8cc2-a1083295172f | -3.12598 | -59.34555 | 2024-10-25 16:54:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 79003bc8-8797-3437-96d1-ad235819db5c | -3.12485 | -59.3444 | 2024-10-25 16:54:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 159621f5-803a-32d9-9363-e09162338a8a | -3.08903 | -59.11145 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 46994447-41af-3108-8214-22ff74e91866 | -3.0872 | -59.11408 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 722dd53b-916d-3adb-9940-ebe7bc359ce1 | -3.08497 | -59.11761 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7b00b8cf-0b0a-3c58-bda8-6c7dde710ffe | -3.08231 | -59.11478 | 2024-10-25 16:54:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 55a3db6e-4d68-3548-961d-17a49671cf5d | -2.84796 | -59.37518 | 2024-10-25 16:54:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d8f0cd99-6208-3c3d-bf5b-a0bb28ffeb23 | -2.843 | -59.37594 | 2024-10-25 16:54:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 04224b2f-4ba8-3977-aaa3-00d727a9e5c3 | -2.72757 | -59.76562 | 2024-10-25 16:54:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25028dac-b3ce-398b-b24e-81d98b516470 | -5.6347 | -61.0479 | 2024-10-25 16:55:38 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c6fb9d8f-03d1-3b2a-af85-9293d3c488a5 | -6.4967 | -61.4195 | 2024-10-25 16:55:43 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 1808ad5a-19ec-3b92-a1e9-426f8e59d449 | 4.47842 | -60.09084 | 2024-10-25 16:56:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 68450847-518d-3002-af6b-3190fc715601 | 4.15879 | -60.44242 | 2024-10-25 16:56:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b032cfaa-0317-3166-852f-3d6db118852e | 4.15876 | -60.44048 | 2024-10-25 16:56:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| db050363-a4e2-321a-b198-11ed8184ee09 | 3.56111 | -60.39616 | 2024-10-25 16:56:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ecfb758d-faa6-3d7f-80b8-487630e71a67 | -19.526 | -56.7221 | 2024-10-25 16:56:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 5ad58dea-2a5e-3efa-849a-b59aede8b502 | -19.528 | -56.6171 | 2024-10-25 16:56:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 7a978c74-0485-3176-88c2-3b1abc2e71c6 | -19.5669 | -56.6744 | 2024-10-25 16:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| b0eeacce-f877-3655-94dd-9a4ed186198b | -3.8874 | -63.7191 | 2024-10-25 17:05:28 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 310edf6d-e82f-3e5b-bb51-49a0488efb9c | -5.6347 | -61.0479 | 2024-10-25 17:05:38 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a08549a0-2e1d-370a-8635-d933da505d22 | -6.06 | -42.7025 | 2024-10-25 17:05:39 | GOES-16 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 7aae3545-bae7-3b76-a08e-97f6a8975fc1 | -19.5484 | -56.5932 | 2024-10-25 17:06:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 96b13eb9-7252-387d-bac0-3c06c2ee24cd | -19.526 | -56.7221 | 2024-10-25 17:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 9979fec5-be1d-3c89-8020-25b7151636c5 | -19.5669 | -56.6744 | 2024-10-25 17:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| dab91072-9186-3a01-a46f-6f072a7037d7 | -19.5673 | -56.6534 | 2024-10-25 17:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| fb3940fe-5381-3b72-882a-c8938b7fb2b5 | -27.13957 | -49.45343 | 2024-10-25 17:09:00 | NPP-375 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| dea4747f-be30-370d-9aac-ea2083b18e9c | -27.1361 | -49.45413 | 2024-10-25 17:09:00 | NPP-375 | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 904ec06c-21ea-318e-b1fd-5ba809c0dad1 | -29.06955 | -49.73575 | 2024-10-25 17:09:00 | NPP-375 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 847915d6-82c1-33ca-a65b-21f93fa7cbb9 | -28.92964 | -49.79809 | 2024-10-25 17:09:00 | NPP-375 | JACINTO MACHADO | SANTA CATARINA | Brasil | 4208708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d6321412-2155-3bea-b4de-57cc809dc4a5 | -28.75411 | -49.6431 | 2024-10-25 17:09:00 | NPP-375 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |


[Clique aqui para ver as próximas entradas](README189.md)
