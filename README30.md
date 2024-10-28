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
| b515a407-9bf9-3786-8911-0c96fe55960f | -2.86189 | -45.46553 | 2024-10-28 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34fbfcfd-34cf-3c05-9c03-a41c80044a62 | -2.79546 | -45.35139 | 2024-10-28 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fa1c3f7a-08a7-331c-aa7a-f573f5b7a570 | -2.79522 | -45.35413 | 2024-10-28 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1b939290-b24a-3ca8-9b46-136b5a5769a0 | -2.23765 | -45.61977 | 2024-10-28 04:04:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f8b2ead-3603-32e1-a421-67cc6740978e | -2.23708 | -45.62328 | 2024-10-28 04:04:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3fe5c6-607d-3ca4-a2cd-44d1cacf9684 | -4.08278 | -44.61215 | 2024-10-28 04:04:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4431b75-e739-300a-8827-f1d9794d8c1c | -4.08209 | -44.61654 | 2024-10-28 04:04:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 424c1f25-ff2e-3d28-ba9a-0bad6d1cd8b4 | -4.07839 | -44.61593 | 2024-10-28 04:04:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 003967b2-810a-3fa6-9dc5-7217ff71cd4f | -3.8514 | -45.72889 | 2024-10-28 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e74236dd-95f4-3dfa-8823-248cb9a83aeb | -3.84828 | -45.72316 | 2024-10-28 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f5a2a0-68c2-3e64-9a41-27e46fe0a31e | -3.84744 | -45.72826 | 2024-10-28 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2730f49-5c7c-3956-bc24-ab83c5ba6a04 | -3.71166 | -45.919 | 2024-10-28 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e32c59d-8510-3327-86a2-016fdb2159f8 | -3.66687 | -45.93428 | 2024-10-28 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64ef2d6b-68ab-34b8-bdd5-fde96ead906a | -3.6606 | -45.39714 | 2024-10-28 04:04:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1244ac8-02f7-30a4-9b18-bdd9c8aa9dc1 | -2.10886 | -46.38721 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad29b421-10e9-3a5c-aa18-78497f57fd15 | -2.05836 | -46.53506 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfd023c9-9e42-3f77-8190-e96143842509 | -2.05407 | -46.53441 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42da2ea7-d911-3756-b5af-5234b0407239 | -2.05148 | -46.53539 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f2faaa0-6f6c-3b56-92aa-44f40d7d9942 | -2.03397 | -46.31561 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95469ed1-fb3f-36af-ae0f-0ae3a2f0d177 | -2.02974 | -46.31493 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81862add-f47d-323e-9fe5-6a276face9a0 | -2.00824 | -46.55772 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a16ec418-bc90-3b16-ad2f-368363a0e775 | -1.95612 | -46.63361 | 2024-10-28 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9fb0808-2691-3eeb-a2c5-44ef6177128e | -1.88929 | -47.04332 | 2024-10-28 04:04:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41f80f97-d26c-3390-8288-c1a3545df980 | -3.45261 | -46.33175 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f3b4f688-6f90-3362-89c8-b3bac11dbefc | -3.40765 | -46.32053 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b31ab4cd-7bd2-3d2a-b14a-90940bb4da40 | -3.40703 | -46.32428 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99a75526-70cc-3a20-851d-298db40a88a2 | -3.40413 | -46.31608 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1b77ab0d-d287-34fb-aa35-d989f315223b | -3.40351 | -46.31985 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0689747-f9cf-30fd-ac66-7983dce34c0f | -3.40289 | -46.3236 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1fe9a7ae-b544-3306-b774-822b518b69af | -3.40227 | -46.32734 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db3ebe09-400f-38c5-9d35-9f056fe7b51e | -3.39937 | -46.31916 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88c44332-4a1c-34a9-90a4-14fb6b70a436 | -3.39874 | -46.32291 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e672a85d-13a8-3041-a16e-01e2240a4508 | -3.39666 | -46.36115 | 2024-10-28 04:04:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96f51ec9-12ff-3784-9f19-40abf1106ee5 | -3.29232 | -46.33689 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a972502f-6f80-3505-a725-e5a83e9c0ff0 | -3.27117 | -46.21829 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c3c6db4-11a3-3aff-9dba-e215cdf5015c | -3.26764 | -46.21393 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24729aa6-684e-33a0-9c85-a859768a530e | -3.23614 | -46.27758 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5547c688-becf-3c5a-a418-75152e6912fe | -3.23553 | -46.28134 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46dcca19-1863-39d5-8135-1068911f7316 | -3.19858 | -46.18044 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45059111-788a-3c9f-9873-c4294a11ade8 | -3.19711 | -46.17959 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da755ed4-4d12-3f46-90c8-c7cd4e200fe4 | -3.19446 | -46.17979 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f68be07-819f-32e2-89c7-03627de9af34 | -3.16899 | -46.61029 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2ddc1028-0d2d-34d8-9957-727f364753d7 | -3.16539 | -46.60567 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89c5e7ea-a864-38b0-89ba-1c18072aa40b | -3.16474 | -46.60961 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 33bf83d8-056d-31b9-9782-129103a3a73b | -2.92624 | -46.79672 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 922d8a94-6620-3a44-8908-879a0520d553 | -2.92327 | -46.78784 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6e0969c-d9fc-3716-88e9-c82b47cbe3c8 | -2.85526 | -46.64901 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28d32718-43fd-3ace-bbb3-644aa7b6232d | -2.72753 | -46.68686 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 828d46e2-aae2-33d4-b147-a0b209a9e3f3 | -2.72687 | -46.69093 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14f337fe-0bac-3dee-8e7c-ab1ff04121d0 | -2.72257 | -46.69021 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 402cf55e-ee90-3078-80c4-305001d83caf | -2.71762 | -46.69356 | 2024-10-28 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9d8ba52-df8d-37b7-9526-80c8892271cf | -3.45111 | -46.1339 | 2024-10-28 04:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f3fa372-4965-342c-99d1-18836eaa181b | -3.44763 | -46.12956 | 2024-10-28 04:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bb7b05f-f83f-3582-bc19-297c3a0eac24 | -3.24127 | -46.0144 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f31095f1-289b-3756-a34f-017625e57519 | -3.23779 | -46.01015 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42f70c96-351e-37d5-9eec-62505adb070f | -3.23719 | -46.01376 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 171d5b84-d496-34e9-b5fb-fb64453153a4 | -3.23482 | -46.02813 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfae9db2-1132-3198-b8a0-85103f6796d6 | -3.23312 | -46.01309 | 2024-10-28 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a62ebd-18f3-3ad2-98e1-dbb9c119e2a7 | -2.77639 | -45.97767 | 2024-10-28 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4237aaf0-279f-3d8f-b882-4ec17e47d01a | -2.74307 | -46.00205 | 2024-10-28 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfec9e6a-12c6-39b4-9666-64882ac31698 | -2.74248 | -46.0057 | 2024-10-28 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98faee6b-78e5-3481-8c35-64050a4a81f3 | -2.73839 | -46.00503 | 2024-10-28 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f23a978c-2119-33ec-8250-fd5334832a2a | -2.55566 | -46.11015 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dd047a6-7d1f-3bb8-8269-22123ad99c2a | -2.54502 | -45.99057 | 2024-10-28 04:04:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aaac3ca-dbb1-3ba7-a90f-641b527486e0 | -2.54091 | -45.98993 | 2024-10-28 04:04:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ead2f3a-dec1-3f97-8b3b-1daff6887c78 | -2.50775 | -46.09103 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 352cf351-d1b2-3f48-9665-50e94605fed5 | -2.27783 | -46.12019 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbf19447-7613-3e8d-936f-a1a0d8445ef6 | -2.41142 | -46.71545 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c53c213-086d-3e10-92f4-f030869f52ff | -2.40844 | -46.70647 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daa8c29f-5a2e-33d8-81c3-17ad2548c8aa | -2.40777 | -46.7106 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84751f1c-bbd3-3916-99ba-d0599da942b3 | -2.4071 | -46.71473 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07a29377-b1f1-3585-8346-da00e7992425 | -2.40479 | -46.70162 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e80e1075-82c2-35a5-9855-6e75aa7f5a6e | -2.35825 | -46.53635 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 872c6b0c-be70-35c7-8977-9751efeae187 | -2.32795 | -46.64348 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ffdf8c4-f459-31b6-a534-82868f03350e | -2.32729 | -46.6476 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee9043ed-e36e-3c96-88b6-798cfc67e2ae | -2.32364 | -46.64279 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2c48d8d-532f-37ac-ae6d-01c87c4ea311 | -2.3197 | -46.4766 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d80526cd-a10c-3023-81ab-6ee85abd4f50 | -2.31943 | -46.50523 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4142c61f-994b-377b-86c0-3f3646cd667d | -2.31604 | -46.66262 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b5bdfe9-8b4c-35b8-9cf5-21283438091f | -2.31581 | -46.50057 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8422dfa6-d1f0-3b0d-b7c4-7c8ad5c52461 | -2.31538 | -46.66673 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aba5412d-a706-3465-8c85-07cb97e8c990 | -2.31471 | -46.67085 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 496ae216-6c7b-38e3-838e-90af9f7aaf54 | -2.31173 | -46.66188 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94bddf06-f796-3b35-88ce-fcceeb5649af | -2.31154 | -46.49989 | 2024-10-28 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a623770-676e-3e47-909a-6016e975a38b | -2.31106 | -46.66601 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7867259c-188b-3d70-a62b-884631be7d56 | -2.30741 | -46.66121 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 801b9e04-53fb-30b7-b065-2d80543a9ae5 | -2.30675 | -46.66532 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5e83532-caa5-323c-8da7-2d3e9bc3d150 | -1.52714 | -47.21064 | 2024-10-28 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de269410-73f4-30e3-a763-9ffe62d46997 | -2.30309 | -46.66051 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43e5cf92-3f6a-361f-8a59-229c86f719db | -2.30243 | -46.66461 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a469a4-4f2e-362c-b1e7-dbc28605c65f | -2.29812 | -46.66388 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32b51f60-fbc0-3731-8fcb-ea7e7717a9ec | -2.29141 | -46.76036 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76f07d51-434e-3b15-b04b-7a8f44bb7e49 | -2.29083 | -46.65422 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93b0ff1b-2714-3683-b7c6-d053997aa442 | -2.28909 | -46.74712 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48ecd8e0-786e-3215-9be8-37a909e2e454 | -2.28719 | -46.6494 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73f38391-187f-3c9c-a10e-394e5bef878b | -2.28707 | -46.75965 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db637a61-334f-33da-8423-94a87369d06c | -2.28653 | -46.59928 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ae70205-dec4-3043-9db9-82a8f01b7e86 | -2.28652 | -46.6535 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8afdb822-1d2e-38c7-939f-8938340ba9da | -2.28475 | -46.74641 | 2024-10-28 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df04d967-fa06-34fc-a6b4-539529c65246 | -2.28431 | -46.13295 | 2024-10-28 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README31.md)
