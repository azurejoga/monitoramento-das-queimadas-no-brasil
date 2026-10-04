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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57fcdb06-630b-3389-a6c2-e06c416715d5 | -2.69176 | -49.03645 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 5cbdcd44-e022-3937-a0d2-28d70f8780b0 | -3.11758 | -53.73418 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37080054-4248-39e1-acc8-396390d744d3 | -2.75454 | -51.55869 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4000576-eeed-3e64-aff1-c0cd9f569359 | -2.81784 | -54.09793 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab86a3c7-d145-3f0c-8632-409b28851672 | -3.11859 | -53.75116 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c68216ff-d20b-36c6-befb-565708ef75b4 | -6.07437 | -53.47518 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59408c10-9639-35f4-8e1d-70c3f119d5c7 | -2.79427 | -54.11038 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d100846-cf9a-3a60-8b25-8218c1b8cee9 | -3.10846 | -53.74541 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 92f5c621-ad83-3470-b98d-d54b6e39172b | -3.30752 | -53.83686 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcc58897-ac4c-38e4-ac51-824a41735423 | -2.59335 | -51.85003 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 68f4384d-cfdc-338e-adcf-ab4ded79008e | -2.91652 | -54.09136 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e15af8c9-3791-39ae-a630-e842ff1b03e7 | -2.81583 | -54.13377 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d2f8e08-f2b6-3d57-b2b0-927150726187 | -3.29191 | -53.84281 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55135179-34be-3fc2-9ef9-f0ec2c0506af | -3.70977 | -50.66251 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6a5cfc8-752c-350c-bfbf-555fc6c2c898 | -3.12902 | -53.73172 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 873366d7-bf2f-3e2e-a121-f64784473bee | -2.99552 | -54.23551 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc709a33-3450-35d0-a8c8-aa61d46878b3 | -2.79197 | -54.10197 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d7cde7f-1fd2-38ed-9fb9-34d1a5498016 | -2.82075 | -54.10241 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11a977b7-8889-3012-a6be-dc7a9fd8bc07 | -3.34917 | -54.17086 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02f104a-3f88-3934-8260-e1d2c791641f | -1.38201 | -55.21192 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6c8db53-6f10-35b2-ab03-9f92c509c75e | -3.17965 | -54.09792 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e048e4-faba-36de-8726-d0f529de269c | -4.23076 | -57.07348 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaec098d-b6c4-3877-b090-bb346b770138 | -5.22653 | -48.40646 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9157c15e-2ef2-3d14-acee-378e40927491 | -2.74805 | -51.54658 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deedcb70-dcd0-3d16-a8dc-8c455d177ad1 | -1.10739 | -54.14899 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 917cad45-7462-3fa6-8369-2d12f0ab9ae7 | -1.27625 | -55.41185 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6c59a5-72f6-3ea0-ace6-5eef39822128 | -4.13172 | -54.16568 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b686dcdd-5800-3b68-bf7a-ac8e3e0d2114 | -1.99177 | -54.10706 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dc5d1d3-6ce9-3415-bb0a-0c38f4287e77 | -3.08612 | -49.5346 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e60e786-e69e-3ca1-8bb2-6931a635f880 | -3.37534 | -50.94424 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be3785a5-bff5-3b8a-8c4c-e2f2e6b9a2c9 | -3.28475 | -53.84169 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a861857-6521-35b6-8937-a712152f05cb | -4.28776 | -50.2641 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| bfe3d03a-be37-3934-a09d-11564a347478 | -2.8088 | -58.32626 | 2026-10-04 05:16:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f6accc-e34c-322d-b368-ce1bac9afb91 | -2.22066 | -53.70533 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| feafc096-a14a-32ab-97c0-3e4200ed7839 | -3.30918 | -53.84966 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 837e8c8b-9244-305c-95f3-18973afdf535 | -3.12607 | -53.72706 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6bcda8a-14f6-3a90-827d-73236b5ad29d | -4.81842 | -54.72525 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c10ec066-298c-39ac-ba69-d5be0fcb9fc6 | -3.00903 | -50.47894 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4537faa-018d-3459-9cc7-91a0255f17a3 | -2.81477 | -54.11757 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b23bc3fd-0d6a-34f3-960b-fdd10a42937f | -3.71043 | -50.65824 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47b24d24-6466-3870-bb0b-82054e4883af | -2.89658 | -54.08022 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09c8765a-7f79-3867-9f5d-c316942a965f | -3.22211 | -54.31282 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e97da528-5f7c-30a3-9d83-ce1a1e71c0eb | -3.52444 | -54.62074 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dc5585e-70f4-31be-80a4-78291493ad66 | -2.34827 | -57.11844 | 2026-10-04 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a6039fd-52d3-35c6-b4df-f0b62289431b | -4.2533 | -55.04196 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 626bfe92-8f1d-3922-aed4-1088fe6c97a8 | -4.27864 | -50.2628 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 22849c57-2709-3d9d-bf08-56814326224a | -3.05759 | -54.16092 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9fdfbdc-65cd-3cb2-ac60-aa1f0669906b | -2.81555 | -54.08953 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e55123fc-714e-3029-a476-46f7cdb07424 | 1.79497 | -55.5603 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9005345-ef07-3b58-940d-633558f7012d | -3.56781 | -51.98178 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05a78074-f0cf-35ca-90c7-df6f0145892c | -3.47506 | -50.09195 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66e7929a-b1c5-3808-852b-1171590a4044 | -1.2601 | -55.77268 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 878c6c94-dc76-36fd-b8b1-377c574f49ef | -3.44736 | -59.6367 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa06fb3-d69c-3a32-9573-22f78382f8d8 | -2.63986 | -54.26636 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857fc267-3659-3f75-b4db-adf68507398d | -2.97747 | -54.09612 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22b11c83-b3ff-3520-b00e-95a39b174072 | -3.04417 | -54.22308 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 17892bd2-990d-3bb6-b420-ce3e3973e2ad | -3.51644 | -54.60388 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d085a95f-ed4c-358f-a741-3217c4496c5c | -2.97409 | -53.26653 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 087e7875-4ea0-3a6b-b007-4ecb7258085b | -3.78977 | -59.37928 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef2ee0ab-85a3-3b0a-bc35-67bb939c3a94 | -1.61759 | -55.01905 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dffa325c-257d-3ac5-9dcd-d4da165b8058 | -4.13003 | -54.15318 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f83fb42-82c6-3a3c-8058-d0539c7f5a09 | -3.07839 | -49.55381 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 97fe6fff-2188-3a80-ab54-a525b14f1e16 | -3.17258 | -54.09686 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16824158-e1f3-3490-8d44-c14051e9542f | -4.27794 | -50.26744 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f4ad2abb-1d4f-3b10-bd4c-baaa4316d576 | -3.58647 | -54.53207 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84e4ea75-d80b-3aa6-8268-959f23f9dddb | -2.59734 | -51.8506 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b04187ef-45bd-300d-a7aa-6789754a8ecb | -2.816 | -54.10971 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ffc08ab-933a-362c-a50e-cac6ed6d1db5 | -3.18942 | -57.91843 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f98a8a84-5d3d-3bff-914e-e8547a682501 | -3.9473 | -55.70285 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 548bb797-f17f-34bf-9c3f-e65fe9a382a5 | -1.40732 | -49.26551 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5603b36-1801-34e8-911c-a6c9ee6b9c97 | -3.30035 | -53.83576 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6449144-a297-3f54-bbcc-0871eea54eda | -3.2772 | -53.81943 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b73b2e52-233b-3915-be8a-ea466bdb511b | -2.82594 | -54.11526 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5648af3-1bad-37e1-a59a-3d75e11636da | -2.80896 | -54.10863 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f43944d1-a76c-30a5-9119-2205fec1cc5c | -2.97515 | -54.08767 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b377622-6eb8-3ef5-8a40-3b9150a8dcd0 | -2.44521 | -50.25454 | 2026-10-04 05:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e5c5cbd2-e6ae-35f1-9e7b-95cee38c93bb | -6.06823 | -53.46468 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eab104a6-5d93-3688-9e87-093eba86e884 | -2.82884 | -54.11972 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 775dbe04-78db-351b-b913-fd5d6bb87ac6 | -3.13017 | -53.73482 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e4103bf-194e-33ea-a933-92641d05a4b2 | -3.86427 | -55.82459 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 516e2009-ddb3-3551-ada0-020cc95010d7 | -2.97868 | -54.0882 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8f60e31-0264-3eac-8b9d-2bad8e31d3c3 | -3.70644 | -50.6566 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c87fe8a0-167c-32c4-a2f1-0c4cd1ec2490 | -2.56219 | -54.96728 | 2026-10-04 05:16:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647a1dcc-d9b5-39c9-9556-5826407d0bb4 | -6.19664 | -52.80327 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 567656b6-cc30-3fea-9b3d-8e2f7e6fd022 | -3.13361 | -53.74925 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b1b95a-bf3b-37c8-9e1b-cd56cd6e4317 | -2.9307 | -54.16199 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03ce4c62-95f0-34e7-9cee-cbb38097369a | -5.73931 | -45.15506 | 2026-10-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d1c04293-bfd4-32f2-86b8-ca45fd670c06 | -2.80605 | -54.10416 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4db90367-7960-3a4e-82c6-2ef26794da62 | -3.01646 | -53.8896 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6fbc205-873b-3aac-a865-71565462663c | -6.45807 | -55.45868 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06ebb856-9e92-36cf-b5f8-fd927ce9c4fa | -6.16606 | -55.37714 | 2026-10-04 05:18:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13b1a1b2-15bc-3dd4-af6b-a7bf20703437 | -11.05157 | -62.57298 | 2026-10-04 05:18:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df857239-977c-364e-bfb8-9834101dd155 | -8.88961 | -66.72718 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a638601-d02b-35fe-addb-d1417ef7194a | -9.92564 | -65.04023 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bd1f7d4-e6e8-3a71-9f4f-0b75ca3c5e2d | -9.40234 | -59.07833 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38b661e7-6c03-3a7a-a258-98832bd62d51 | -9.08679 | -63.98439 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0efdd4fe-ee0a-37bc-b56e-9aa74647e5ea | -9.14855 | -68.23545 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc226a4e-5848-30ed-8bbc-567355c85c87 | -9.54249 | -68.53047 | 2026-10-04 05:18:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ae3e134-9dff-3beb-baeb-438d90a6d69e | -9.16976 | -61.40424 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eae62495-4526-3e3f-af97-3d16e272521a | -8.58771 | -67.14272 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README63.md)
