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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a842269-c3bc-3939-868c-27618f638509 | -10.85986 | -63.92639 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39d51b3f-0736-3ab2-9a84-c40e3c39719f | -10.8593 | -63.92992 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d550d873-ecfd-3906-b457-bf8c1c444bac | -10.85823 | -63.91529 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb7710c2-48e1-3a4b-b70e-25a524b9f6ea | -10.85773 | -63.89714 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa1018de-c217-3014-a3f6-c5d291fdeacc | -10.85767 | -63.91882 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57165402-affa-36c4-b1a0-cff469d440db | -10.85716 | -63.90066 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 095d1b35-acbb-30c4-b101-ac4d1b459c88 | -10.8571 | -63.92235 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4edd68b1-2fd2-3bf0-b6a1-4a499cecc841 | -10.8566 | -63.90417 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81dae641-29f5-3a91-9661-a32d990c3ad9 | -10.85653 | -63.92589 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8aa824d-95e6-3bcb-bb8e-9c5548497b74 | -10.85604 | -63.9077 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beca15ff-4ea9-3ea4-9a36-b7023d8cb380 | -10.85547 | -63.91123 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 693218ba-e640-36a9-aae0-e80d221ae1ba | -10.85491 | -63.91476 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d7e054d-3c07-3ad9-9e42-e56f64087fe7 | -10.85384 | -63.90011 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4278844b-8833-3958-bfaa-6db6728a002d | -10.85377 | -63.92183 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efa646f6-efcf-380a-af23-eefc75ff9d0d | -10.85328 | -63.90362 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a22d893-e7d9-3bfc-8a7a-590c69c881d6 | -10.85272 | -63.90715 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1835d02-602c-3cdc-95d6-e3d2138d0c33 | -10.85215 | -63.91069 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07ed501e-00a8-3327-97c6-9073b98e948a | -10.84939 | -63.90661 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04d9c8a0-f4fe-33f0-9e4e-7c683dcfbb06 | -12.08628 | -64.67177 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51193c3b-c74d-3d94-97c2-a0ea34172a35 | -10.99693 | -63.89808 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffdc389e-550f-32db-95ce-77a359f00a3a | -10.98073 | -63.93547 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 735f55e1-0915-31e3-abe9-dda2bde88a7b | -10.97683 | -63.93848 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59854866-704d-3dd3-8907-2dad5deaf1d0 | -10.97351 | -63.93795 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c897ae76-17c5-38b5-ab53-3c2f7fc5f1d7 | -10.97294 | -63.94148 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cffea7c5-bc32-317c-8e45-a84502581fe2 | -10.94031 | -63.87083 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 162d35d9-93f2-33b1-a643-ffb564141aa9 | -10.93644 | -63.87376 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e8ff1b-cf3a-39aa-bb11-ed2eb66222d1 | -10.93587 | -63.87733 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 121f218a-11a8-319d-85be-a2a8c9c07eec | -10.93142 | -63.88392 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0874d29-becd-3d7a-80b7-2ad6a5919ae9 | -10.92433 | -63.84284 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ca9963-fc8f-3a5e-a73a-78d765ae4086 | -10.92377 | -63.84633 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 511ba3a0-6dac-3f9c-bf07-2a86e1223aec | -10.92101 | -63.84229 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683ca942-a316-3c0b-9712-4e5b8233be52 | -10.91146 | -63.90222 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79975b68-e487-38ef-a401-c1b53ffa18c0 | -10.9109 | -63.9057 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebaa1302-81b1-3656-b324-074b1b23fa78 | -10.90757 | -63.90517 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ab9db40-1dba-3798-8846-c296af0ac32d | -10.90701 | -63.90871 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bd7358-1b71-3561-a7a3-6454eb045310 | -10.89888 | -63.85285 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f998f1c8-c246-35dd-8bb0-23462081fa41 | -10.89867 | -63.91826 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ccc653-5456-36e6-a6d7-2e9b0ab87d2c | -10.8981 | -63.92181 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 130c0847-d7d9-3006-bfc1-c1fc402c799e | -10.89479 | -63.92123 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e81e2a29-6762-3547-8ced-67a4801729ba | -10.89309 | -63.93184 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3824c84-de48-3aaa-85bf-f4b40d4f7c7b | -10.89034 | -63.92773 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ee11e10-de8b-3a94-aaf4-05c14cc1bc54 | -10.88977 | -63.93129 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f74bbdf0-a587-348b-81b7-fbaea3d877d6 | -10.88645 | -63.93073 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae43aca6-a968-3552-8df1-615364413ae4 | -10.88588 | -63.93428 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ab9218-e6bf-3e74-98a2-6439c1181861 | -10.88256 | -63.93373 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51d951a4-b05b-3017-85bd-74356c59949c | -10.87924 | -63.93319 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eff466e3-e1eb-3a1e-b07b-bbf53ac8a129 | -10.87866 | -63.93676 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b37e811-cf98-34c5-b6ff-9ed4c865eb7a | -10.87591 | -63.93266 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ad1f9ce-d75f-3ae3-ab7e-591b64e55921 | -10.87534 | -63.93622 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d896593f-3860-3d32-a0d8-c432fbb4fbed | -10.87258 | -63.93213 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b9cb970-3ab6-35c5-add3-fd20750d913d | -10.86926 | -63.93158 | 2024-10-13 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40f109bf-bbff-3897-826f-86784638cd2f | -12.02434 | -64.71358 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db5c94f7-6158-351a-a03c-b4c1b24b64e0 | -11.96148 | -64.7703 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1797b1bb-506d-3d07-b1be-e8ccd90d3799 | -11.9587 | -64.76609 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb9aecc-2e34-3bc8-bfbe-38ab8c689912 | -12.36761 | -64.48845 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bba87b99-a734-3aea-915b-5c724b5275d5 | -12.36342 | -64.32222 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac9d5ae-651d-3469-8300-67af57344b60 | -12.3601 | -64.32165 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09cfa47f-2e05-38e6-b230-3cb687230718 | -12.35953 | -64.32515 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22f9950b-dd87-3cef-8277-24add7a11714 | -12.35677 | -64.32107 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8da9d11-4567-3b3c-8f33-d8e13caf1a76 | -12.35621 | -64.32458 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50322343-4028-35c0-a09a-b8a58c1dafae | -12.50332 | -63.9342 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4082287e-b373-325d-b07c-bb75118f01aa | -12.50164 | -63.94479 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fb026e7-85dd-363f-8d7f-398aca2fb8a8 | -12.49833 | -63.94425 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1b8d1d6-7474-345e-b0ba-066776563904 | -12.49777 | -63.94778 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ecf209-dd18-3352-8ca7-67aa355cffa2 | -12.49445 | -63.94723 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30608eb9-0aed-3644-a1bb-74e13f133d0f | -12.4944 | -63.96896 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39359665-78e9-37dc-9292-f0caede1564d | -12.49389 | -63.95076 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9079dda-fbef-3152-b412-55edcd8c2dda | -12.49002 | -63.95375 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd95c187-794c-39b4-a1cf-6f26c5bb1da6 | -12.48833 | -63.96434 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0972d74-27c4-3859-a7ad-606d92fa7383 | -12.48777 | -63.96787 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d5dda1c-f7c7-30b6-a30a-1aee20f168f4 | -12.48615 | -63.95674 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98063ee3-7247-3b0c-8dff-a0b01f3f0670 | -12.48559 | -63.96027 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e2c907d-01ce-3d9d-9eb4-4d761b75d653 | -12.47526 | -63.89701 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4346c9e-d058-3a9f-8446-e3501d280cc0 | -12.42652 | -63.99053 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e47a52c-b773-3805-80cd-610b8991d8df | -12.4232 | -63.98999 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6fa74103-a361-3b08-ae55-ac5fd3e43c27 | -12.39558 | -63.73587 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 071a4c8f-3460-32af-8df2-20927df9ce89 | -12.39502 | -63.73938 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2be06eb-8126-3d84-a356-e6643e19f798 | -12.39394 | -63.72477 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a0edeba-c587-38a5-8c82-4f1524124521 | -12.39338 | -63.72829 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24ad41c5-25f9-32c6-9bd0-34eaa7fe3bb3 | -12.39283 | -63.73181 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b7db97e-911c-378e-8f1b-da3bf1ec07f8 | -12.39227 | -63.73532 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1f2a0e6-730f-3ff9-ad5b-f3ffb8b5bb9b | -12.39171 | -63.73884 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5817496d-b7fd-3960-bb64-6ca61d95a031 | -12.38991 | -63.72747 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e60cfe7-abfd-3605-8a79-2616bdc720c9 | -12.38935 | -63.73099 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b510466d-ec41-3335-914b-d260641b093f | -12.3888 | -63.73452 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a247058a-e1a9-37b0-b3e3-96663533460e | -12.38824 | -63.73803 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88ca164f-71c5-3e25-954b-df7a3a7e9154 | -12.3866 | -63.72694 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99e30d85-e0df-35ff-9e43-3d95976d6014 | -12.38604 | -63.73045 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 810fa620-f854-379e-b16d-11eaf645b6f9 | -12.38549 | -63.73396 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efe38bcb-ef54-37a6-8623-a978dc316c0d | -12.38493 | -63.73748 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71ec7440-ba4d-3e82-85ff-7183e1a901df | -12.38438 | -63.741 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f336526-e8a3-3956-bb98-17c4c017855c | -12.38218 | -63.73343 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc47c43-9864-3fd7-83f6-5670c1a2bd64 | -12.38163 | -63.73694 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb45edb-1067-3417-a098-e395dc0131cc | -12.38107 | -63.74046 | 2024-10-13 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96ac430a-0986-39c0-8239-b4fd9ac5c107 | -10.7474 | -65.07317 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 858a0753-856e-31fc-8543-438837cee824 | -10.74397 | -65.07259 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72ffef49-ccb8-3245-8990-0dbdedfc094e | -10.73994 | -65.07574 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f80fd2e-9732-3d9f-acb1-b86900c7d5c1 | -10.73652 | -65.07519 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70268c31-f1f5-3682-843b-c60563567791 | -10.73591 | -65.07891 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09b80fb9-3ca9-3847-adb1-d991f07ff56e | -10.73529 | -65.08276 | 2024-10-13 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README110.md)
