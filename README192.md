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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d605d35-ab2c-38f7-b391-8395a0d89a63 | -3.04244 | -54.2566 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3485a60b-305a-3ae2-96bc-dcdffe513fcc | -2.99582 | -54.0668 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb30d552-ed15-34a4-870e-5e6eadffd739 | -2.98606 | -54.13234 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08b81f51-4be4-39a9-b0e6-48a88e11973c | -3.48854 | -59.58764 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 155e2463-1c4e-32bc-bfad-a87dda149032 | -3.56901 | -54.35963 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9d17f5-afbe-3d6e-a599-1d593f72ebd8 | -2.93825 | -54.0605 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef8f463b-57b6-315b-af05-da49e4bd274f | -6.99776 | -59.10979 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f883e36c-f2cb-3113-82fd-22780113d343 | -3.57865 | -54.65466 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 798da272-e57c-38d6-a186-beb97621d1f3 | -3.11426 | -54.17205 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3cafa6af-7e8a-39c6-bcd1-3bf296a5c388 | -3.09243 | -58.02707 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4b0c39ae-39d0-39c2-8c92-d8ea461a5690 | -3.17858 | -50.56203 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3df9b38b-b123-34d9-b5a4-4b301744736b | -4.34611 | -55.13227 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f49f3e32-c781-3bab-b20b-f266b82591bc | -4.15603 | -55.13912 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8706fe3c-10c1-37d8-bc34-5d953c05223b | -3.0898 | -53.95104 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fafe6aa4-72e6-39ed-895e-f10d94958a37 | -3.55718 | -59.47376 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 859ecc66-69fa-3da6-abd5-a2a88e8f2aaf | -4.92272 | -55.86919 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d10a2c-1f1e-3515-bc86-bc7a9720ee13 | -3.28949 | -54.07001 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 433b8b4a-33c4-3792-8742-10f3b1305e71 | -3.53948 | -59.50498 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 148ad0e4-5a2e-3f33-bd82-c3aac48d01cd | -2.94321 | -55.79173 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39e95f48-f3bc-3c99-beb2-9bd175073ab3 | -3.53576 | -59.50442 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32fd15ca-ca5a-3855-a7ef-5c6dbde821d0 | -3.01745 | -54.10365 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8707b14d-7bc9-378e-8068-673cb4fdd849 | -3.06483 | -54.25042 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35fad9c4-862c-3259-9d6b-a2c4bf82f8ee | -3.72148 | -54.23294 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de9fb9b4-771b-35d7-8515-49ccf1c34f91 | -2.4705 | -56.06959 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbb4cab4-ccaa-3096-97b6-b83702f62901 | -3.6698 | -60.63044 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4676b57-20ca-383b-85e5-c5e156445a3c | -2.78517 | -54.07743 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f4cae62-8b5c-3d2a-a72d-229f827f31ca | -3.63001 | -55.51481 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e84a3f9c-4c89-35d9-80dc-3d9a5f4a7ad3 | -3.51625 | -54.6693 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 935b3c36-9c8a-3ee7-b3ee-725db9e54ae5 | -6.46727 | -55.48515 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c72e5b1c-82f7-38bd-9d0c-a58daf6747d3 | -3.00733 | -54.09878 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 431170c8-5b78-39e6-afed-e491ba807ee5 | -2.99663 | -54.13405 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cfac709-0da0-3cf2-9dbf-74baa5a95616 | -3.289 | -61.00364 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da2f5e65-5429-3116-aec8-ad4b4b5ded9a | -3.96198 | -56.11742 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a96ad73-ebf1-38e7-8f24-a01d907d30d1 | -2.76685 | -54.09133 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5273c5d-3e1b-3219-84fc-4c8dfe7889d4 | -3.17513 | -57.09245 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f47fcf5-3db9-304a-b00a-31054a05e4e8 | -3.62817 | -59.28554 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f9d57cc-e69c-350b-9e20-e5ea2dc935bd | -2.93875 | -54.05721 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7efcd20f-bf11-39fc-9179-f7db931c9ff0 | -3.0974 | -53.72055 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e32d2fd2-5343-3bba-9e3d-49b542b979bc | -3.56465 | -59.4749 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1525b14f-23c0-3605-a315-0393c2745570 | -2.57182 | -56.17365 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff02c2bb-6c99-37c9-bd55-e149e48391e9 | -3.07912 | -54.29869 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87ab7207-11d5-31b4-b3f3-f5c18a9cb4b0 | -3.72587 | -55.49144 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf1104bf-dc43-3759-afbc-36ab510be366 | -3.00154 | -54.10124 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65bdc6e1-002a-3856-b434-709f5a983dd4 | -3.09036 | -53.73026 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8585638-faa5-372a-8d99-f239d4db52f0 | -3.29391 | -54.01916 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd105b67-e5ea-3727-8c92-918403ad8e22 | -4.4445 | -54.97812 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f56106c8-5e75-3fa3-9bc4-1b837aadc926 | -3.28462 | -54.06595 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d9e6c1d-a569-3b07-a045-0faced70dd95 | -3.70421 | -61.32571 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab4bb3f9-7bda-3313-86c5-24cc2f2ecd56 | -2.86205 | -59.30913 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80a0741-4ea0-3b81-9e55-9246292bdd65 | -2.8975 | -59.20419 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ba27437-7cf9-3ac5-ae67-62cc54c4a933 | -2.70525 | -56.54761 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11302b96-e497-3944-b11e-31ed3f3dce82 | -3.30171 | -54.02377 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b717101e-8816-3ef5-ba6e-f7c9a345f969 | -3.00261 | -54.05771 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 66e84ad8-2f24-3b18-b12f-aa8b22d92f61 | -3.75927 | -59.46878 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc1c4bd6-7470-37e4-8699-cf1946892221 | -7.38284 | -55.22313 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d45fc74-551e-3d5d-8cbe-083600f66722 | -3.02057 | -54.04681 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ff3d5a9-1b96-3b5f-8c3f-ac508edc3558 | -3.58575 | -54.67756 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7ee01ee-29ea-3a40-97fc-30f0c025fed7 | -3.59723 | -54.56579 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e77ee4e-39cc-341b-bc11-d8b6abe9d174 | -3.53687 | -59.50715 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e126a75-6d3a-3e6a-b302-242dc42e5792 | -3.73429 | -51.21099 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85cb7a75-9460-39dc-a51c-1a3b361993b5 | -3.35205 | -50.47593 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1aedfd93-371c-33fb-a59a-ac2732c37c8e | -3.07263 | -53.95569 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b966ffbb-8dfb-3944-8530-7b49e128a530 | -2.1696 | -54.46014 | 2026-10-08 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e02f731c-7019-3602-b7f2-b85c028286b3 | -3.18724 | -50.57103 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ad6572-4cc7-39d0-9542-1a10fb7f3d2f | -3.31001 | -54.69997 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84058163-0f07-3a52-a1e4-1817914d244f | -2.96554 | -57.76622 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e3bf15b-b1e1-32b0-aa1f-dec38c89acf8 | -3.01524 | -54.04604 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a906ef84-fa5f-30e2-8669-d0fe1a570a54 | -7.89809 | -54.72259 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86421055-8a07-3524-a8a9-af306d3c9100 | -6.48833 | -62.85752 | 2026-10-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ebde5ee-8e9c-3686-925b-0b872adc6c8b | -3.5333 | -54.67668 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d61dacc9-c69b-37a7-83e5-e3eab35e4629 | -3.28318 | -54.07583 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e1e73aa-2d87-342c-bade-da70c12b6a30 | -7.20579 | -55.10754 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc363d23-742b-38d8-a523-79f9ef66abc0 | -2.93664 | -54.17711 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20813241-4c04-3ca9-9676-24b0de7de51b | -2.82425 | -57.60803 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e12fde7-0b94-3686-a859-d28b16d9a059 | -3.28218 | -54.0452 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03fbe061-56f2-30e8-9b6c-4a15bffd31df | -2.99197 | -54.05606 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd19b3b0-0b04-3c32-a5ce-cc49f31a52da | -2.98953 | -54.07255 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9fcde843-ef7a-3ba4-94f7-cee04560ecef | -3.28852 | -54.07666 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d69b012-0754-309d-a091-24e0d1a147fd | -3.29097 | -54.0223 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec94197d-e9b8-3c44-baf8-730830c7df65 | -3.30359 | -54.0483 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae7f31ba-0269-3e65-a9fd-4f8e573d9584 | -3.01941 | -54.09062 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae666b6f-1276-3985-96a6-b92dbe454a39 | -3.00769 | -54.13243 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69fda135-857d-3b73-8c30-7bf704072d6e | -2.49854 | -58.0737 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9221606c-5029-363c-bdbc-6cc90874b4fd | -3.19077 | -50.54792 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8685b256-b0e2-3d3c-a074-b5392c34577e | -3.10609 | -54.19043 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e20e2681-83cd-3270-afed-4e4fc01e6023 | -3.29236 | -54.0293 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a5dfd67-63a8-38c7-8510-9a448d93c5b4 | -7.22973 | -55.1683 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35d7e253-3598-3c24-af1b-5f86f0f1158a | -3.28906 | -54.01508 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c784a75b-d76c-3f21-ad0a-958836daa400 | -3.17504 | -58.63195 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9b8e7e42-7eec-365b-aef5-aea3f244e3d4 | -3.14261 | -53.72357 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4c2d11e-8605-3717-a2d9-137ccfade239 | -2.48772 | -56.11073 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce53ab51-be2f-3ba2-af91-003f1514e190 | -3.13795 | -54.36905 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb111f5c-751b-362d-b4e9-8a99b0bdb43f | -2.12316 | -54.80284 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68895e6b-fb54-3d9e-a379-7e5ce1406886 | -3.1014 | -53.76738 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab36469b-a449-3c94-b50c-8426eb8c873f | -3.01857 | -54.06011 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4a43d7f-e760-3809-bce3-1d74a7c1f3b9 | -6.98875 | -59.11547 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02ce317-955e-3480-bba0-d55b66dac77a | -3.11399 | -53.7939 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53ee50b7-d8a8-3dba-80ea-00778b32fa15 | -3.29155 | -54.07016 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8995c069-df23-392d-acf9-aa6532929c2c | -3.58066 | -54.31874 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a45d711-68b1-330e-9cfc-7a1e1308714c | -4.12115 | -59.87438 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README193.md)
