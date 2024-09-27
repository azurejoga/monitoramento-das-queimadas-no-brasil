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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e38910-d581-39a8-9d03-c0fc62cc66ed | -11.49568 | -59.44927 | 2024-09-27 05:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80ac2a12-755d-3de9-8237-389651f4bf05 | -6.37074 | -59.96226 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28b4bc6d-ba09-31eb-8cb7-6e9277cf16b8 | -6.36543 | -59.95429 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79fc057a-389b-38db-8506-c293ced637a4 | -6.25743 | -60.01793 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3943cf69-f667-31b3-b08c-39da308be403 | -7.27887 | -59.66163 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a3acbe5-98ba-32fb-878e-b96eadcab2fc | -7.2725 | -59.49131 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14f2d0cc-6011-3187-8df3-35ac3a504ff6 | -7.2719 | -59.49525 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63c636f5-16ec-350a-acba-abbe231c816f | -7.23715 | -59.51036 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3266d0fe-9644-3261-83e1-d49f667652f6 | -7.23656 | -59.51431 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d129abe8-6cc0-313d-a581-9a54d75c8b3a | -7.23363 | -59.50981 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d16c0fe4-5fd0-3150-8bfd-74f698121607 | -7.17393 | -59.4494 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd2bec6-5d08-3442-92f2-81ebf8110332 | -7.12514 | -59.22525 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a3304d-d7b3-3fe9-81df-b9ddf1fa2e88 | -7.11916 | -59.45337 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a79727d1-4776-3e6e-8510-f894316bf686 | -7.09429 | -59.76177 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa87bfc0-362b-35ae-b1a4-c5946682c90f | -6.98974 | -59.94626 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87570aec-5b4d-3cc6-af84-a59745d3ab94 | -6.98893 | -59.5997 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a31016a-7719-325d-99d9-3f5d4818b17c | -6.98834 | -59.60361 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cef1c11c-cf8f-32e5-8374-dc338e2282e5 | -6.98542 | -59.5992 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab3974c-6853-3a12-84cc-1059d1becfa7 | -6.80221 | -59.30209 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01e8e015-c0a9-3e39-997f-d93537010d27 | -6.80161 | -59.30609 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ffae6fd-246a-39c9-beeb-73f7b3711350 | -6.79872 | -59.30229 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d2dcca4-ad32-3088-8382-eb2b162a47f3 | -6.79811 | -59.30629 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f2fc6ab4-3287-314e-8467-9b065dd22e22 | -6.79807 | -59.30557 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb65303d-0b4c-3034-b570-b360e2384482 | -6.79749 | -59.31028 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54790153-8bde-3a4e-9896-189a1b71b342 | -6.79747 | -59.30957 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bace52fd-ea6f-350c-bdca-fbc85856e3fd | -6.79457 | -59.30576 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 52513230-5097-3bdf-acd0-4a0d8d80d85c | -6.79395 | -59.30974 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbb63f82-ef98-3dd7-8c4d-8ce83784fedf | -6.79393 | -59.30903 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d0cc82e-3219-3354-ad11-2a23803ac790 | -6.79334 | -59.31372 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af5f00b8-dfe8-376c-82c5-b67d3e06cb2a | -6.79334 | -59.31302 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a117be63-7070-3312-9fb6-0637c40989f1 | -6.79042 | -59.3092 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d36c20e5-d8f4-3128-8048-7fa3081f4e20 | -6.7898 | -59.31319 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 672d927f-69a5-3ebf-9a37-7f703f312f60 | -6.78688 | -59.30866 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cd7fcd2-bcaf-3f22-8ac6-fecd66b3b5bc | -6.78659 | -59.3576 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb8ba60-7f73-3370-88a2-7ea389bf2f15 | -6.78622 | -59.36095 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6067b413-dbae-3056-8ec6-03e4f0b9dfb9 | -6.78598 | -59.36158 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 874f87ab-4615-3752-beb5-2f07653186e3 | -6.78563 | -59.36492 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4359f890-eb63-3c19-b7e3-0abb87e7ffc2 | -6.78538 | -59.36553 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1d0d236-4c03-356a-ab96-a15b9a143281 | -6.76558 | -59.69027 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8596c644-bc74-35a7-b597-052e93dc9a7b | -6.765 | -59.69413 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 933a9cba-e3c9-37ae-bc08-7e8f94ec10ab | -6.67146 | -59.78246 | 2024-09-27 05:27:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e1c0a2c-b250-3946-bb69-0a98ef544b37 | -6.64143 | -59.95612 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426c5e96-a10c-3e87-bcf7-cba1fdb1e3ae | -6.64086 | -59.95989 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4591b34-88b2-3ff0-8a8c-a81f66a7a7ae | -6.63799 | -59.9556 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b734fd17-07bb-3cad-8719-0897271bbfd6 | -6.61217 | -59.9401 | 2024-09-27 05:27:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97ced3ee-cbe5-3ceb-9075-489bde31e436 | -6.60873 | -59.93958 | 2024-09-27 05:27:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96321355-7981-30ff-9c87-2de7f52d5d49 | -7.59889 | -60.58808 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33b87140-de67-362e-a7cb-c42806f090dc | -7.59834 | -60.59171 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebab2bb5-5e18-3687-89de-87e0bd4ffaad | -7.59779 | -60.59536 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2139cf9b-7394-3dd2-9a16-3f0ae69d1c97 | -7.59723 | -60.59901 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5169819-4923-3468-94d1-289e5ac2a09d | -7.59662 | -60.5802 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 498994d7-bc59-32ca-976a-5badf86f25ac | -7.59606 | -60.58387 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba6701a2-89f2-317e-a9f2-68e5d76a0db2 | -7.5955 | -60.58754 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 7e332a8f-d4e5-3483-b25a-f162f887ac25 | -7.59495 | -60.59118 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 0d156c9d-a247-3624-bb4e-1fdb8ac51830 | -7.5944 | -60.59482 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 88e205fe-b32b-3199-beaa-c0804a878c8e | -7.59384 | -60.59848 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| deed569f-3948-3c88-814a-dc80aeb45f9b | -7.59328 | -60.60214 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70dfa5c3-5e74-38d0-9488-6fed697f437d | -7.59322 | -60.57967 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faff574a-1533-3c47-8680-e0c3e836462d | -7.59267 | -60.58334 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46df7a66-328f-3028-92c8-2ae95d323af0 | -7.59211 | -60.58699 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 4e256eed-7fd4-34ad-a4e2-a7c92a6be0f3 | -7.59156 | -60.59065 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| a4e206e6-e052-39e2-97c2-2d46cf388806 | -7.591 | -60.59429 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ee56037d-c815-3a63-b5f3-ee880e0ac1bd | -7.59045 | -60.59794 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 68e0fac4-7e52-357b-a13c-d613c1fba59d | -7.58989 | -60.60161 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| abcb1b6d-97d7-3100-a7bd-c87f908b81bc | -7.58983 | -60.57915 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06dcedb0-ace1-3656-bbc1-c826f4b4dbf1 | -7.58927 | -60.58281 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cc83eb6-202d-3a2e-8395-82e651d7b5e9 | -7.58872 | -60.58647 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 77880def-fd86-3e55-8ab2-0f69498d179b | -7.58816 | -60.59011 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 431e5cba-a07d-39e1-b557-b6bf2421b741 | -7.58761 | -60.59377 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 554fefd5-55e4-3f6f-ae76-fccb759e13f7 | -7.58705 | -60.59742 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7b7f2c20-daa6-383f-b2f5-4b0fecba41e4 | -7.5865 | -60.60107 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fd0f3eb-a481-30e5-9f4a-94852f1588cc | -7.58643 | -60.57862 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4a7f93a-bb6a-3542-a34d-0e1ed9d65d52 | -7.58588 | -60.58228 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43e2e22b-fb61-3260-b3dd-907c48b17449 | -7.58532 | -60.58594 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2a4a8972-f053-3fa1-a5ef-9e649e1b85e3 | -7.58477 | -60.58959 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 81ca42f5-94ba-312e-942a-492fd5c66df6 | -7.58422 | -60.59324 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5e8f8569-b688-3e3a-aeb6-96d1f4404894 | -7.58366 | -60.59689 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| dc08415f-29e9-309b-a337-f5906a46bfac | -7.58311 | -60.60055 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e078c937-a9ac-3cc8-ac42-1e4eca331be8 | -7.58248 | -60.58176 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 385eef3c-30c6-3be4-8827-b547905b427c | -7.58193 | -60.58541 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 419bbfe1-9fcf-3f05-8796-37d3dd2e108a | -7.58138 | -60.58906 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fc0a977-26a0-32e0-a5f1-5f00040df60e | -7.58082 | -60.59271 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25755cea-f6ff-351c-9968-1ba161026abd | -7.58027 | -60.59637 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a9e1f8-154b-3d18-bd1b-7e4ef52c867b | -7.57854 | -60.58489 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49526382-ba1a-307f-989e-8834a7558f67 | -7.57798 | -60.58854 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be69d701-8ae8-3e0f-99c2-3707f2c6854f | -7.57764 | -60.58572 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4fa36fe-a274-35a0-ba29-1fec659bbb1b | -7.57743 | -60.59219 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c4432c-2136-321b-aa37-9d3c17da4117 | -7.57708 | -60.58936 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e22419ff-6733-3a80-bf8e-4c7bba9cea0d | -7.57651 | -60.59302 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e76159-b7c9-3357-86a5-f6f86a26b265 | -7.57594 | -60.59667 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a74040cd-3eb7-399c-8651-843785d1b5ed | -7.57255 | -60.59615 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6294c065-ebe0-3f66-a6cc-7379ded95993 | -7.57199 | -60.5998 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 3a140d08-554a-3a7c-9cba-c943ad1c4b9e | -7.57142 | -60.60345 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 925daa61-e600-397c-b198-831830a71fc8 | -7.56916 | -60.59562 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9826b51c-914c-37da-a73f-1d3828345186 | -7.56859 | -60.59928 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe3474c5-1491-3346-9980-89a371c94159 | -7.56803 | -60.60292 | 2024-09-27 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f628ff39-d310-35dc-a61c-39c840664197 | -7.49584 | -60.6664 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca8ff2d9-000b-3782-8838-b32496e6b3cf | -7.49528 | -60.67007 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 575f83ff-5db5-369e-b511-dc739a536286 | -7.49481 | -60.71833 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1846281-e0f0-3f5b-b450-b3c7e3d4184d | -7.49246 | -60.66588 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README120.md)
