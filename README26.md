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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d8b05a8-e2ac-3d9c-9b58-563196c384c0 | -11.31455 | -47.00834 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e559122c-58e8-3d81-be59-90e48743e694 | -10.71685 | -52.11057 | 2026-08-16 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c0df495-3c3e-3dba-9c20-8b5a4c71d314 | -12.00538 | -46.41932 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 50d89320-0f59-3bca-a2da-74e67b975d79 | -6.82859 | -45.34599 | 2026-08-16 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e088218b-0dc2-3b4a-92a2-500cee7e30e2 | -6.82656 | -56.45117 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fac0e039-0226-3f1f-b38b-d14c55dfde66 | -6.71839 | -58.92751 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41d265df-a9c3-3b53-9942-f27e77c5a1b9 | -8.94714 | -60.51662 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea7f3176-f9a5-31b5-9664-f2a59f995872 | -6.71892 | -58.94054 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fb6562a3-d401-38af-a32f-41f5dbda7af3 | -9.11026 | -46.38694 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 296ac857-8e35-30c5-8558-edfafd521a01 | -9.35253 | -62.37075 | 2026-08-16 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55d9608a-3029-304a-a4bb-5584ed90002b | -9.09004 | -61.40291 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f50f192b-2d43-32f2-8c3a-d48a08d54206 | -11.21897 | -54.82207 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b113399-8850-33bf-8995-9c4e9da47706 | -11.33785 | -46.21629 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7099d39f-15f7-3ce5-9abc-3e5be1945156 | -11.89562 | -50.22816 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bea75775-a6ae-3c8c-bfb5-23cf06754716 | -12.03629 | -46.43761 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| debcf19a-7aa1-3692-a413-6807460a0b34 | -8.90326 | -60.55562 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53e9024b-e7e8-39f6-866d-8f11505cf116 | -6.62015 | -59.07489 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 577e62f6-bd9b-32de-9c9e-687386f43948 | -6.92766 | -43.63304 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a826b8a-25ef-3c8c-90a0-2f3484790cbe | -11.88323 | -50.61574 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 598b0fd5-2e62-3b93-b271-bb2de1642c90 | -10.53427 | -44.85495 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d733e624-696d-3475-8e55-23aa89adb197 | -11.33852 | -46.21153 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fba33caf-ae83-3521-9bdc-3291abefe54d | -8.89175 | -60.55359 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcca64e8-b578-3220-8074-5821cb5bd02d | -6.83121 | -58.97829 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e486510-d031-389a-88da-f19c4d8f978f | -7.42462 | -60.03026 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 130dc002-4fe8-3426-b865-5c5608c48b25 | -6.6094 | -58.97931 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 320fe004-4c23-3311-889d-27abf5d929f1 | -5.25522 | -47.70974 | 2026-08-16 04:40:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d08c6d7-2195-3788-90ca-27d958b7c2d3 | -6.96293 | -59.28488 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6deb02f4-27b5-39d4-8dab-1bfe9288878c | -11.4814 | -46.59406 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e4a8c80d-9c62-30f3-911f-7c337face78f | -8.64539 | -54.71854 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9db16264-6211-311a-8bc8-1efd5a318feb | -12.68821 | -48.45041 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a42a0e6-117a-3ea4-a3e8-eabe0312f608 | -12.70295 | -48.47983 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6297c0c9-ffb7-339f-a35f-8d0c5fa998f4 | -14.31822 | -53.05693 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c374b05-aeca-3f51-bf58-ff137e1b624b | -14.46452 | -51.99956 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57358343-c629-31ba-8de6-49033a612c1b | -14.39804 | -51.88247 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 55ccec5a-6f1e-3397-aff7-22da587c6367 | -15.04494 | -47.02121 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7198d0ec-d566-3b95-8084-a6934f4aee01 | -14.41087 | -51.84434 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60023a88-0427-31e6-b16e-f8956c00501b | -15.16243 | -50.06591 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1868c7b3-fe30-3bab-b25f-60fb700d0e69 | -15.0467 | -47.01795 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa59c445-602b-3ff9-8c2c-409650965891 | -15.03702 | -47.04993 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e7a5c58-f18a-3993-87d8-f9e2aeb00759 | -13.42007 | -57.0486 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33b482fc-4e58-39e9-8e99-1ec146866965 | -12.71511 | -48.46986 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 797eae1c-f752-3831-bef2-1afea6859a01 | -13.80292 | -53.82803 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2107f574-0800-3a88-b01b-0c2c82acfd3e | -13.78102 | -53.82503 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d79fd38-79c1-3e22-92d7-c83bb75ad94e | -14.40079 | -51.88659 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0012c9c6-0969-3387-b2db-1223a681554d | -14.80964 | -48.29778 | 2026-08-16 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f298cf87-b565-31da-bb3a-f8f0eda98c2a | -15.09988 | -48.71998 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aaf0525-add8-3a82-9b46-6067f869ab3f | -13.8152 | -53.77669 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f970458c-a952-39bf-bf9c-1de137f7803b | -13.53786 | -46.24775 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 207a1784-ced3-32d6-914f-595cfacb8e24 | -13.80554 | -53.82925 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0244f1bd-c33a-3639-98e4-77b15635c7b9 | -14.38307 | -51.89096 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46af6775-8bde-3743-a517-9560871ca6eb | -13.50772 | -48.2353 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b45dd332-8188-3c38-a284-a17b40882153 | -13.52986 | -46.24694 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f34d1f77-d4f0-3716-b6bb-3f00e8dc5945 | -12.72964 | -48.4683 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cf3ee7d-db44-31ea-977a-87fd26c24caf | -15.15716 | -48.67227 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e3591a5-68d4-3685-8df8-1032c6a28e08 | -13.794 | -53.79001 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55720bbf-2504-38b4-b6a5-0b958408f49e | -17.66972 | -50.4853 | 2026-08-16 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3832456-1540-3af9-a8c2-af1b57b4e791 | -17.71528 | -48.65516 | 2026-08-16 04:42:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5ba9d29-4e76-3c00-a044-05f39d0dd999 | -13.53386 | -46.24734 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1176373e-4f58-328d-9151-8bd652caca91 | -18.9573 | -47.32197 | 2026-08-16 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c15a6080-9743-3bba-ac23-ae7767a8263b | -14.41442 | -51.95111 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f0ba674-b4ee-3384-b8e1-8a347d29bc06 | -15.35124 | -49.61266 | 2026-08-16 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be69be4c-9ed0-31e7-bc48-3f7504b3df26 | -13.54585 | -46.24858 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b54f421-84db-3037-9e91-b0a9e5407f2f | -13.5012 | -48.23001 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abefee86-74bf-3645-adae-eb7e58bc0424 | -12.68006 | -48.45713 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b3d790b-9bd4-3118-8ba2-91605e9b9de6 | -18.30338 | -44.50519 | 2026-08-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07f2fa95-ec19-38dc-a25f-725594f32160 | -12.68882 | -48.44634 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88a65473-a54b-3fd9-9f3f-495948366257 | -15.05896 | -47.01483 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3fe3584-4424-382f-a7d3-02025d98f2c7 | -13.70769 | -51.88116 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2ce633d6-e4bb-3151-9a19-1700d9fff414 | -14.06952 | -53.68887 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1acde5db-89f7-3717-b921-3f5c8b19b18a | -14.33962 | -53.11839 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8425ca3a-9c34-3748-a3aa-e9f4249ad7c6 | -13.24485 | -54.18617 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1896b849-00fc-3618-9459-3ef05189f43e | -18.31645 | -44.51784 | 2026-08-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c65ce99b-bc9c-323c-a9d1-4899ab6cf22b | -16.84698 | -49.43423 | 2026-08-16 04:42:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d49c751-fe9b-3525-bd9a-c961b473d7ba | -13.70437 | -51.8806 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 503d832f-9fb3-3d24-b882-183088603b92 | -17.66916 | -50.48911 | 2026-08-16 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57c6d087-fd5f-3423-a06e-f3fc9bfa1b1e | -13.75097 | -53.43203 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5479b46c-80a9-3aa4-96c0-065d61b43603 | -15.69769 | -47.4624 | 2026-08-16 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 979776f4-1adf-3409-a59a-6257a79c54c3 | -14.42363 | -51.82818 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94b7b7b1-8a4b-32fe-a1a7-8d7321b330d7 | -14.76195 | -56.35646 | 2026-08-16 04:42:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d01a5c87-0fe3-3ed7-9779-bd8e3694559e | -16.88818 | -54.16193 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a992ef9-e94f-3e80-b4e3-51308dede900 | -14.31482 | -53.05638 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32b9949d-800b-338c-a821-4cdb44772888 | -15.1194 | -48.68498 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f499f834-5d7b-31f0-a9fb-3d5181549486 | -15.05824 | -47.02035 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b6444d9-b449-3a42-a4cb-bd7a3d81e74f | -16.66911 | -49.13858 | 2026-08-16 04:42:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4611ae72-fce0-3b89-9eaf-8ae26afc8c0b | -14.48065 | -45.6902 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b66c5d48-26a1-3df8-a9f8-ef42defedd57 | -13.79618 | -53.79862 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9206cc22-d6da-32d9-b918-5950275d77ed | -13.81256 | -53.76467 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78af4911-6a59-3834-8f4d-94f79da2c9bc | -16.88259 | -54.15285 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc71ec28-76d0-34cf-a618-3badd7c2544c | -12.72267 | -48.46707 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 173657fe-630c-36f8-a706-9fc903f91152 | -14.90442 | -46.64105 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8401af6c-0769-3ec1-9257-1ca8e8d28220 | -14.30063 | -53.05784 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d1b55f5-5e7b-3f28-a787-34383882a071 | -14.93631 | -46.61355 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f36ad168-9246-3fa5-92e3-720def70d06d | -12.0582 | -58.04273 | 2026-08-16 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 884653d2-2afb-3683-9c6c-a41769f8402f | -18.57225 | -47.15552 | 2026-08-16 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac9a214b-ef10-3db9-9c6d-b238146fb20c | -13.25093 | -51.67375 | 2026-08-16 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03aac47f-23c7-37b7-9ee0-a57ee2b140b7 | -14.29116 | -47.19086 | 2026-08-16 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48b04edd-1df8-3d97-bbb5-1544f5a103f8 | -11.58398 | -54.68939 | 2026-08-16 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3501750-68bf-3fe5-99d2-7cd83eefbae8 | -14.37919 | -51.89397 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f242878a-d7ac-31d8-9ce1-669aa7572e46 | -13.50655 | -48.21797 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66f83989-441a-3c41-9ec0-162cc6cb1429 | -14.22473 | -51.81689 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
