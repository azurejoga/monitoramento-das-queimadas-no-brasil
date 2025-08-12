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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ec98e0b-5bad-3a1c-bcb5-23a271fcec66 | -11.69209 | -51.58962 | 2025-08-12 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a045d31-9c65-36ce-872b-aea636e9eaff | -11.72913 | -50.10729 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b650f216-edd8-323e-9aa1-a49196b59f89 | -7.14093 | -60.12035 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d2a07847-6f2b-302d-8f36-e745ebe793e0 | -9.03421 | -59.76295 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 808c348f-fee5-3465-94dd-373d18c3491e | -7.12979 | -60.13256 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 715e6203-e230-312c-a9bb-7af19420a5bc | -9.88575 | -55.39595 | 2025-08-12 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 270611cb-b048-3422-abda-d75c3283beec | -7.06859 | -59.18554 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec36a688-8f0b-3a5e-86cd-7e7135342b30 | -6.96746 | -59.28029 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 605cb291-46cd-30dd-9b67-c98035b79499 | -9.93258 | -60.48003 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ea42a0e-aa89-36aa-85c6-c7989e1225df | -9.18661 | -59.66079 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb588696-6f09-3497-af4e-5d3c0c7fab41 | -8.93014 | -60.72853 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28918cf8-3cab-3150-9ec7-3b9dd4927256 | -8.9252 | -60.75996 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd9a7027-6876-3e3d-80b5-3e334dbe98b4 | -9.37458 | -61.53388 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca2538c9-30ea-3a35-8a83-da088808bfcf | -7.25602 | -59.99529 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b64f4b91-270e-3030-b7e2-27bc790ae6af | -9.37569 | -61.52687 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9967b31-989c-3452-84ce-d01144609146 | -8.56912 | -54.69233 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b4b231-4eb6-354d-b49b-863d50aa3ab5 | -10.75675 | -48.78516 | 2025-08-12 05:25:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20e176e1-4cfb-3515-bcc1-0bb4a5427fce | -7.13864 | -60.11965 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1e6928ee-209e-3773-8379-82f644446c81 | -9.26333 | -60.78114 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56eb6dfd-2248-3b1b-8b70-a54ba7eab69c | -9.47086 | -57.83975 | 2025-08-12 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e5c8796-c6ee-3498-8bea-cb73718e1661 | -8.56474 | -54.69169 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01b4af81-24cc-30a5-ad22-1c41edfff585 | -8.56535 | -54.68743 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aa4e48e-a05c-3420-ab02-c382d0823e77 | -7.06634 | -59.19997 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd9a1168-8fda-37fc-a734-47ad9fa8c4c2 | -9.1804 | -59.65607 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9085144e-f3ab-352b-af7e-0652176c0e4f | -9.20015 | -59.66286 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808c8481-e074-3e04-85f3-e559424e0810 | -3.43556 | -49.04505 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 818b6983-8fa1-33b2-a6a3-27d501d08693 | -9.37402 | -61.53738 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 260f1630-03e2-30cb-ac90-021ab2c01441 | -11.7314 | -50.10934 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c417e251-9e09-3361-8030-a61d2a9a7283 | -9.93482 | -60.48763 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b586d506-e334-32eb-abd1-3f8b73c35f3b | -9.68453 | -63.5984 | 2025-08-12 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 533602db-4b39-3870-afa6-5212ce2b4d0f | -9.38567 | -61.52847 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 855df28d-3ba9-3e62-9898-ce1b5701c9eb | -9.37625 | -61.52336 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dbf385e-42de-3737-89ac-0006fe48a422 | -10.04644 | -64.89777 | 2025-08-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af334363-8929-3dbb-8e61-affaa0cf8ad7 | -8.93624 | -60.73308 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1678b41e-3bca-339a-9d01-a9383a12d2b7 | -6.97646 | -59.28905 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55a0479e-5285-39d5-ba92-e6f02c7e897a | -10.74315 | -58.01472 | 2025-08-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03410d89-3418-3975-a6f9-2cb7fa927954 | -7.25548 | -59.99879 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9919cf1-7a36-3baa-9cb3-70d7c5f1179a | -7.07041 | -59.2001 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d9b2dc7-ee50-38f6-9a04-5a0b2b57fc4d | -9.38899 | -61.52901 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cde9d5d0-d770-3de5-ac93-a5d40aca3462 | -8.93682 | -60.75106 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e751c4fe-a4c9-3e01-a19f-92875f16ad9d | -7.08449 | -59.19855 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62deb0e4-9b14-3d49-85f0-83d2399e80e3 | -7.1393 | -60.13081 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 68b33dd8-5fd6-3bd5-b73b-31d3450c524b | -10.00776 | -59.21524 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac8a822-34a0-3be2-8da7-6dcd306f22a8 | -6.10833 | -59.93281 | 2025-08-12 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50952f3-cf6a-3ff0-ad69-2fbc717f479d | -13.90282 | -51.83339 | 2025-08-12 05:25:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1bb7f1ab-fd7a-3bec-b48c-b578c40b847a | -8.93295 | -60.75403 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85f0ea7b-d1fd-33ed-9361-e96383c4d6f4 | -11.72857 | -50.11219 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed4ccb93-5d29-37b3-8a51-a8a67718b951 | -10.35693 | -50.82077 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d5080e5-4efd-35d4-b2db-cd53963b42cd | -8.92853 | -60.76044 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 668a0f98-efab-3ab0-8e76-1fa47c8f8964 | -10.6268 | -65.00795 | 2025-08-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 071aa2f1-3296-35e2-a3d6-4a808e884890 | -11.6907 | -51.60119 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57302ef6-cf1b-31e7-96ed-d775a06f5cc8 | -13.06906 | -56.84498 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bab42838-cd57-3b53-9a7c-5b871daa05a0 | -13.34876 | -50.25287 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 92ead4e5-98ad-3d7f-afd0-6fbdefff62a6 | -9.37236 | -61.52633 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 251470d0-6197-3997-ad55-f40f00af99e9 | -9.47082 | -65.6029 | 2025-08-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7cb1498-6e62-354e-afe7-b985bf861b8f | -8.93241 | -60.75748 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b662a9d-7b4d-3144-976b-7f92d654c752 | -13.35506 | -50.25355 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 217244fe-e087-3a43-9210-bf1feca59efc | -11.67759 | -50.13734 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9065c2ed-324a-3bf0-90bc-1c8f6abac759 | -9.5383 | -66.1407 | 2025-08-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f8c2e31-8d39-3946-ab83-b8c38a109014 | -2.58784 | -51.92133 | 2025-08-12 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26859ab3-40db-359f-ad00-734848ad6913 | -10.97372 | -49.57296 | 2025-08-12 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58cdaeb1-45a0-39ae-99b7-7261826c65a1 | -13.343 | -50.24734 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bc8a5ff2-d420-3c82-8714-6bb9fa14bf4a | -11.68924 | -51.5904 | 2025-08-12 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44815b36-34a2-34da-bbd8-befb599d0a5f | -8.55902 | -54.66903 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43c7bd84-b1d9-345c-8cc2-803a6f742043 | -8.72404 | -63.13972 | 2025-08-12 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19f301d5-ec76-398c-90db-1254194e19a3 | -10.35747 | -50.81652 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb5eb9c3-0cbb-35e7-a30c-36e394548421 | -9.19338 | -59.66182 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| acc384ee-dae3-3d2f-b9a0-9cf35c30643e | -7.14262 | -60.13134 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| aaace67d-c0f3-3547-9aad-bafa12fd735f | -10.97432 | -49.5678 | 2025-08-12 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18661112-de98-3d1c-8b6b-dfc0bc3e0853 | -7.07662 | -59.20473 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 63efe2a6-9b63-3387-9723-5728f78a2b88 | -7.13644 | -60.13361 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7de6532a-b1fb-3fe2-855d-eab6ec7ceede | -3.83645 | -47.75027 | 2025-08-12 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 227497de-0dd5-3e23-80a1-09adec331107 | -10.62234 | -65.01176 | 2025-08-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92b95a20-99e7-3581-9922-eac694941b98 | -8.5673 | -54.70507 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37fcfba2-bcfb-3477-9eea-2b7c4f9799af | -7.07607 | -59.20833 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a8ad209-79a8-329f-b011-c0e6c90f1822 | -3.42895 | -49.04852 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f91ab16f-0691-35ec-8efe-d14388def20b | -3.43623 | -49.04065 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b915c86a-4e9e-3f4f-a681-2cc68e6bbe42 | -10.31622 | -54.15564 | 2025-08-12 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc080adf-74c1-3218-ab99-52c11f336ecb | -7.07773 | -59.19752 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5dc9da0-7afc-33e5-b02a-afb1b0afa9de | -10.35005 | -50.8282 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94c0b45f-45ab-3bd9-b2fa-cc457cf224d0 | -6.9602 | -60.13089 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b3b27d3-a019-39de-a26a-ae77f4571392 | -8.93237 | -60.73604 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21d5c990-4c3f-34c7-ba21-03b0890fc89e | -8.57545 | -54.71056 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3401f854-5d5a-3c5b-a4d9-f21ca7a2e1b9 | -7.25214 | -59.99825 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbeea846-9b2b-3f65-bc6d-696fb0c36ed7 | -10.6305 | -65.00858 | 2025-08-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8cd613f-c4c2-3ef9-a134-69bfadef56cd | -7.48178 | -68.33719 | 2025-08-12 05:25:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4bbb23-98d0-36ce-829d-a8dcd5fa262d | -9.03537 | -59.7636 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4a3875f-67a1-3ab6-b0fc-6effa7b5bbe2 | -8.90849 | -60.5452 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36a52f06-3a4d-323a-bc73-399ae3c87335 | -7.81962 | -61.32741 | 2025-08-12 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78c63654-f065-3d57-bf49-434c59fda104 | -7.13144 | -60.1221 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf2190c2-3c5e-320f-8d23-b3f39514933c | -8.93569 | -60.73657 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e1057686-70c4-33d5-98b4-fc59104e40ff | -9.18267 | -59.66389 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc9c1cba-e307-31dc-957a-5618189d23b6 | -8.91747 | -60.76584 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f13f6d0-137b-37f9-af88-2c2703e23937 | -9.38067 | -61.53845 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 457b0570-3a37-3591-8dbd-12ccd1d8189e | -10.34371 | -50.83145 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab201e13-1965-3540-bc1d-b51f58b7079c | -10.75975 | -48.78458 | 2025-08-12 05:25:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ba0ad99-045b-35e2-be33-31779a21f37e | -6.96353 | -60.13141 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 440f329c-2937-30b7-a50a-8d0105d78226 | -8.56608 | -54.71358 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60939319-d087-3d95-9b70-f9b18e8943de | -10.35057 | -50.82412 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 674ea205-d3b0-3fe7-b549-1260a06a057a | -9.19676 | -59.66234 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README31.md)
