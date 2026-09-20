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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd15488b-a615-39e4-8dfb-490301a1da9c | -9.84 | -46.4136 | 2026-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 08217b55-30bb-30ef-ab43-6a0daab5b55b | -12.152 | -47.0383 | 2026-09-20 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 212.6 |
| f6e1bc9d-6d61-3d8a-bb52-0816a9b95452 | -8.8636 | -45.9596 | 2026-09-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| b0792159-4996-3c7d-9e33-a75f1f6d8581 | -11.949 | -50.1186 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d8129765-59a8-38c3-9071-79305abbbeca | -10.3914 | -48.9133 | 2026-09-20 14:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9e1d03d3-77db-351a-b189-9aba7763e865 | -8.4376 | -46.8757 | 2026-09-20 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6b4a5b38-b450-377a-a55f-b40c31da4c42 | -3.1079 | -61.408 | 2026-09-20 14:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7c3098e6-b9a3-309f-8655-020561752a21 | -9.0541 | -48.7686 | 2026-09-20 14:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 676.8 |
| ea565eca-7d78-346d-a5e4-7618f6f30a32 | -12.1524 | -47.0158 | 2026-09-20 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5846f204-756a-38ab-995e-2651bf6d26e2 | -11.155 | -42.7885 | 2026-09-20 14:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 259.5 |
| a484ef76-2f31-3105-a062-52e39cf2f284 | -11.9352 | -49.7752 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b1e7aa0e-59e6-35cc-acf5-07d2db3b1b38 | -7.0286 | -45.2554 | 2026-09-20 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1af08e0c-a40b-3bb5-9c48-16e102ba6b6c | -7.3289 | -55.2155 | 2026-09-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 253b57b5-841c-30fb-9d9e-6331535bf024 | -6.3198 | -59.9572 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 514cf7f2-e76d-3b8c-9375-0df0ad93cba5 | -8.2499 | -61.3724 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 773f7f16-28ca-36b3-a1df-991a0e2fa6a4 | -11.4924 | -45.3608 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 4f0b3168-79c5-3a6c-8714-7b5985ef3dd9 | -11.0596 | -54.1755 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| dbf2a846-e98b-32de-a301-0ee556a46b98 | -10.8757 | -57.1554 | 2026-09-20 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 314a828e-0643-3c70-a5ae-7791b2d3a7ea | -7.7301 | -44.6892 | 2026-09-20 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6d3b6537-4ea3-382f-829b-bdbf9925f32c | -7.693 | -44.6469 | 2026-09-20 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8cfb8e6b-ac44-3532-9aac-b6b7e1c0e08b | -8.1686 | -54.7634 | 2026-09-20 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 7a6c8e5c-5f4e-3ef1-91ce-63941c574d62 | -17.5795 | -44.9765 | 2026-09-20 14:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 7fb375f0-a29d-3c6e-bfa6-35b1b041eae8 | -8.4312 | -45.8693 | 2026-09-20 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c5e9aeca-213e-303d-98f6-06edad36e770 | -11.6429 | -47.7761 | 2026-09-20 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 761baeac-2cb9-35ab-89be-77f9e071a636 | -11.0802 | -54.0302 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| a74d0599-5d84-3a35-a667-e5f69acd1ad6 | -10.8367 | -50.9266 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 3353770f-7b86-3342-b17a-4f18b3a6ad2d | -2.9157 | -57.7983 | 2026-09-20 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 553a7f79-0618-35e6-8b55-d368214e4f46 | -5.8088 | -55.7095 | 2026-09-20 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| b69a34d4-9b31-3474-9869-9d45a57b19b1 | -8.8825 | -45.9576 | 2026-09-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 972394a7-68f8-3c6f-90db-a7fc667732dc | -11.6621 | -50.2169 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| a7d7fe91-ba3b-3d23-ade3-1755276b0298 | -11.8744 | -50.0199 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 5e32cc56-12b4-3ac0-971a-96f41be60fdb | -12.5081 | -50.952 | 2026-09-20 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 44451257-a6fc-3f29-95d1-4388dda4b4cd | -11.8747 | -49.9983 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| fe83ebd0-610a-301c-9c97-34b67d59f6d4 | -11.9493 | -50.0971 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| b362e3e8-a656-37b8-89ab-52484b752788 | -11.6609 | -43.4239 | 2026-09-20 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 0276e7a4-b46b-3200-b0cb-876d808a3a31 | -8.4611 | -57.6292 | 2026-09-20 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ddf827a1-2f08-3cd3-8328-c30560e119c1 | -6.3199 | -59.9381 | 2026-09-20 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| c0f98272-5df9-312c-bb7a-d798634c8ff8 | -8.0892 | -55.3511 | 2026-09-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| bf8a068b-7009-39a4-bc19-7a8d6ca31dd8 | -10.2598 | -50.2624 | 2026-09-20 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f859955a-e86c-3e03-8988-e77f68d44b52 | -14.6861 | -46.6657 | 2026-09-20 14:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 680352e0-67e1-37a4-b7c7-19a3524ad4b5 | -11.4549 | -45.3202 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 70009002-c6cf-3901-b079-2e5c4185eb1c | -10.4673 | -45.0873 | 2026-09-20 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| a7319987-08f7-3d95-9fad-28d44d4829ba | -11.0994 | -54.008 | 2026-09-20 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| ae686079-50e6-3975-8253-7416145a4a01 | -9.26 | -45.9616 | 2026-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 655.1 |
| 5946cfe7-88c3-31c1-8f92-4c726b9ac80e | -10.6694 | -50.7103 | 2026-09-20 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 9ee4c4f1-fd7f-3e79-bccb-4527ac5054e6 | -8.845 | -45.9391 | 2026-09-20 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 27d1fdeb-dbf7-3730-813a-65359b47b7cd | -7.2519 | -55.5994 | 2026-09-20 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 94e4637f-7b12-3cf7-aa83-ee0a7181f1cc | -6.9225 | -42.9088 | 2026-09-20 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 93537e25-9b3c-3525-8fd7-ddf33e3cb990 | -9.9058 | -45.7965 | 2026-09-20 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| aeea84ea-0619-36ab-b35e-d6fe65ed280a | -12.9084 | -51.01 | 2026-09-20 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ae4f88ae-6bb0-39c8-9604-54161e1f2610 | -11.04 | -54.9 | 2026-09-20 14:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8a2dc2a-8d54-3c65-987e-132a8dd5f803 | -6.9 | -43.74 | 2026-09-20 14:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f1fc183-18dd-307d-ab46-4052e1994339 | -14.15 | -45.55 | 2026-09-20 14:15:00 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18ed3d7d-e40d-3b73-a82a-ca46e879b6bd | -9.24 | -45.92 | 2026-09-20 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77e26c19-cea3-30c3-acc1-6d3694274cd3 | -14.12 | -45.54 | 2026-09-20 14:15:00 | MSG-03 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 154be727-499f-35d8-b97d-e47ac383f5e0 | -9.27 | -45.93 | 2026-09-20 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33fc853f-248f-304c-a0b1-bcbf11c4218c | -9.27 | -45.97 | 2026-09-20 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26fc9e52-15fb-394b-affd-d4a068bb2b2c | -14.7 | -46.67 | 2026-09-20 14:15:00 | MSG-03 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62feb1ae-dd9b-3b34-8ac5-d193c67a46d9 | -9.87 | -46.45 | 2026-09-20 14:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81d1d1f9-b1d8-3860-b8b3-cf4b59f80d2a | -10.35 | -50.23 | 2026-09-20 14:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fab5815-6cc4-3f2f-b903-397dc2bdb53d | -7.3073 | -55.6163 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 97719cc8-1b6c-3d48-9055-3f6de0535505 | -11.9352 | -49.7752 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 46cd184a-0856-33ca-b4a1-66bb637831a7 | -10.4673 | -45.0873 | 2026-09-20 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| fa92d21f-481c-3855-88e6-fed8f47f61e9 | -3.3493 | -59.8479 | 2026-09-20 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 01740040-0ebf-3abd-8e3f-dba8c056b677 | -11.155 | -42.7885 | 2026-09-20 14:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 138.1 |
| 8e157c93-9b82-3c7f-ba40-c8552a94d627 | -10.8367 | -50.9266 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 238.5 |
| a3958365-fa70-3f33-bb26-53cb5f2e0550 | -8.1874 | -54.742 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 3dfe9f03-9220-37e3-927b-8438bd770873 | -9.8502 | -48.4053 | 2026-09-20 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 68cc4fa4-1633-3a8d-a528-918cf13d439a | -11.3793 | -51.3989 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| c7417a0a-74b1-3aec-9741-0f437c7f5830 | -9.6964 | -45.8666 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a036a1cb-74cd-39c9-9406-75624b58eff3 | -11.731 | -50.7014 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 7d15e007-96d2-3c54-9c91-2b90400cf7a7 | -10.4541 | -51.2827 | 2026-09-20 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| cfed00c0-9cb5-38dd-8073-be17fda6ccd0 | -11.379 | -51.42 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 86ddb01c-fff7-31d6-a381-c664ab604be3 | -9.8397 | -46.4361 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 2523f6dd-432d-3602-86e0-5562867183c1 | -3.8814 | -40.7251 | 2026-09-20 14:20:00 | GOES-19 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 149.5 |
| 2a3365cf-4e24-36ef-9ecc-1ddd14d5eaa6 | -11.8744 | -50.0199 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 11ccba19-27b2-3c1c-b4e5-750e583ed311 | -7.7444 | -46.7184 | 2026-09-20 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| bcfe538c-ae29-39a0-a6ff-75ff3397c02c | -8.7729 | -44.2568 | 2026-09-20 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 313.3 |
| 50615cff-49b1-3f07-ae1a-db94808b7c41 | -11.0506 | -54.9309 | 2026-09-20 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 231.9 |
| e2cdeb7d-767c-3856-8baa-48c1cdb283f5 | -10.67 | -50.6678 | 2026-09-20 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 409b6f2c-e98e-3d83-9aea-2faf3dc2394b | -6.1981 | -55.4534 | 2026-09-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 507ca371-c391-3051-a23a-9a91e55e2b59 | -12.4171 | -50.6636 | 2026-09-20 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4141d510-1455-35eb-87b9-fc94501637ee | -10.2787 | -50.2605 | 2026-09-20 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| b8d5338f-35a4-3c8a-920d-47b1354ff83e | -10.9692 | -57.208 | 2026-09-20 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 82fb40a8-0018-3c94-837d-b5c99bd3ce0e | -10.6694 | -50.7103 | 2026-09-20 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 45d4aff5-6afa-3a23-9c01-74a3ef06da52 | -11.9349 | -49.7968 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1bc4c631-bb54-3ee7-a515-80e4bd27cb93 | -12.1328 | -47.041 | 2026-09-20 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| b25103d3-427c-3e89-864f-5f55285bddca | -8.4922 | -47.0257 | 2026-09-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bb7589d7-7d47-3e0e-9fb1-7e854d042951 | -6.7369 | -55.0874 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| e8fbedf2-7e7d-3b03-ae1a-4de6107ba700 | -11.3609 | -51.3585 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e08b62b8-8e2e-346c-af01-e11403a84b2c | -8.0706 | -55.3522 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4186359e-c8d7-327b-8b4d-f58461b45575 | -11.3269 | -47.2833 | 2026-09-20 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f90038d0-b08c-3c9f-941f-550b4a19cc2f | -12.027 | -50.0015 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| b8072222-2e18-312f-a821-a50c4531d4cb | -12.8704 | -50.9933 | 2026-09-20 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f83246f0-9955-37b5-afab-13a2f04879e1 | -11.8747 | -49.9983 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 834ca89f-136c-3660-94c3-81a858a6dce6 | -9.2606 | -45.9164 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| c4476c32-05bd-3cfb-a61c-8b4972bbee1b | -7.0286 | -45.2554 | 2026-09-20 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 6fe9ec70-47b5-3a6f-82fd-341d8b198866 | -12.2344 | -50.1488 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 224.8 |
| c364edd4-70d9-3075-8627-1038812c3e88 | -11.0256 | -48.3164 | 2026-09-20 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 2146c542-046b-3bd9-8678-b684a11a30e6 | -9.26 | -45.9616 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |


[Clique aqui para ver as próximas entradas](README126.md)
