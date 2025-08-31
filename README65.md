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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc282cb4-728a-387d-9017-0b1e4d0ce2bc | -8.74821 | -62.38186 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13479d35-0785-3086-8b1c-78b58ecdb9df | -11.32618 | -43.66125 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f81e136e-d4ef-3649-a8a1-22a5cc78e6b7 | -11.07525 | -44.62805 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c08ea5fb-0934-3a46-833d-a193792ae7dc | -13.46861 | -46.97431 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a760812d-469b-3edd-bfe0-4b82cfd51862 | -11.01522 | -46.96103 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96aa21c3-e12e-39aa-9c5f-1d66d344605e | -13.47215 | -46.96826 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c820ce7b-1a11-32d7-a61d-8270bbdc9c89 | -8.84748 | -52.0233 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c4bea67-8aaf-3511-85ad-968c4138a83d | -8.68936 | -62.87924 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48e6edd5-4fa3-32b9-a708-3c8c52413d87 | -13.46167 | -46.97612 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a8deba0-aec2-31d5-97ea-06a837e93ec1 | -14.33497 | -51.87263 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ed0d796-c32e-3594-839a-6ce757d538c9 | -11.32664 | -43.65739 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e05a9e7f-02b3-3763-a660-99708be6c0ae | -13.02513 | -56.89731 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d2e0c14-f5c7-320c-a2e7-1253d4c71605 | -13.68669 | -46.87462 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc1d5120-f80d-3eb6-8658-c6aa1878baff | -7.91592 | -63.01122 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 94eee1f3-deec-3cf6-98ad-588318a04f8a | -13.30287 | -46.9131 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0299311-6495-3a1a-81fd-7b1c63e97239 | -10.08286 | -48.87634 | 2025-08-31 04:51:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16bd2058-6410-3950-8592-f7d31e294e0a | -13.34712 | -46.97498 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26c7a72e-7688-3d83-8039-5a968d787eb0 | -14.53954 | -51.9795 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0b4376b-39f1-3329-8285-cbe40b49731a | -10.03659 | -46.02083 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24c799e3-e6bd-3a7b-82dc-6d0999e5b5a2 | -8.29817 | -46.31519 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e8438ac-6394-387a-b52d-1144287dbf7d | -10.41522 | -50.85948 | 2025-08-31 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b2e81e9-0912-3e3f-99d5-c5de1fc9befd | -9.45961 | -62.33641 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bd50337-4032-35f4-b35f-90a3ab2465d4 | -8.64221 | -62.82629 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 646fbeb0-3571-3d96-855e-4afe358dc644 | -11.55892 | -47.62125 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 430bd5f7-e1d4-3b9d-ab42-2e5cceed1d85 | -9.438 | -62.36577 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d4e49ec-d2a6-3a8b-adfc-c4626b7128b0 | -14.03335 | -44.56912 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94c26895-bc5d-33b6-8bb6-3b10bc5746f1 | -14.27861 | -51.8852 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd95c5c0-139e-31a6-95b5-d6300ef2c2dc | -11.28345 | -63.24433 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2c504eb-047c-34fa-a374-b71c937f4f55 | -11.35358 | -43.62551 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8b06e86-7945-35f3-8343-7d903d786bf7 | -13.35441 | -46.95578 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d44a529-4536-3bf8-ba03-17e7ff4bf100 | -9.43931 | -62.3294 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1de877-e72e-3599-8d4a-838291382349 | -11.06026 | -52.05345 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d5378f-5825-37b6-905f-f23fe7898c60 | -8.74274 | -62.39113 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f3cc7b9-ed47-3a71-9c4a-3e9333092c91 | -14.33849 | -51.87315 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ebaa217-1e31-3cec-9f2c-e9196f558cc6 | -14.33556 | -51.8686 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8d7edf7-bee9-3434-89c4-9317c17d95af | -11.01834 | -46.86759 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae1cd5b-522b-3d1b-8fdb-64fc82e1ccdf | -12.26848 | -59.34618 | 2025-08-31 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1320362-fa40-31df-8047-39d5fe177d38 | -9.44382 | -62.36353 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a9d215-4d65-33a9-99a9-581218148012 | -8.543 | -45.80931 | 2025-08-31 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fccd199a-1685-3ec7-82cb-8b219b533b10 | -11.94252 | -46.68937 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bdd2496-a709-3700-87eb-0fc569716302 | -11.90919 | -46.69033 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f986f3e1-b1a0-3947-b3e4-e3f9b1904181 | -8.73699 | -62.38325 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea50d9a1-a455-30dc-bc4a-8b77b0ff07fd | -9.44919 | -62.33436 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 245b9e94-5615-36a7-9cea-5e3efe6d32e1 | -13.00902 | -56.90686 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fcfd0bb-7388-3dd7-8b3a-7eeda0dc2495 | -7.92151 | -63.0123 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69e4e3fc-be28-3bb5-a92b-ff816c81e572 | -10.03488 | -48.08864 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d5586e70-0b3d-3229-afdf-88e699c7cf63 | -11.29943 | -43.66796 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 269528e2-539d-363d-894b-4bd86ecc05a6 | -11.32429 | -63.26338 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c3cdc4bd-d7bd-340b-b368-bf1fb7ae5867 | -11.31352 | -43.69287 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83eba676-fcba-37d2-934d-b727edaa52b4 | -9.4607 | -62.35994 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12b9629b-b3dd-352e-aafc-3e93876c405f | -11.8849 | -46.73195 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df4162fd-e22a-348c-9521-bb6979140ce7 | -13.0097 | -56.90283 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e7ca26f-4a20-3544-b40b-2ac66d1a2f33 | -13.35118 | -51.76376 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbc44719-a429-32be-9b60-3b39b3efb09d | -13.97488 | -46.31892 | 2025-08-31 04:51:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63496875-91e4-3455-9747-0fc04c6abc41 | -9.30484 | -59.21814 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9efa23e-20fd-3927-b1ac-53d784deee44 | -9.44786 | -62.371 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f39fb7a9-5065-303d-b41c-8ffcbb7c0016 | -13.32904 | -46.85799 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a5efe8a-140c-39e8-9af1-4e8b796b3039 | -11.06026 | -44.61898 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6daf4460-6c9a-3462-bdd0-a39b023b0c24 | -10.95086 | -50.8518 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 03e501d2-505e-3dbf-9be8-280c20e67943 | -11.31774 | -43.68353 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9e50011-0e46-389b-9683-106c265e186c | -10.32189 | -59.19355 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84ffaf00-633c-3c6b-808d-9a3d9c0d4cda | -13.53967 | -46.96111 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8b1f2e7-24d0-3fa5-869e-0e7bf7dcd82f | -13.34585 | -46.98466 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0bf7d72-57ff-324f-abe5-b221c6f5ce63 | -10.42228 | -50.86055 | 2025-08-31 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 954dba2f-ec99-3617-b97c-8d5fdf5b823c | -12.80042 | -48.08937 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eaa4b5f-1a0d-3c10-bddb-0a87358d5a25 | -12.91783 | -56.97562 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3eca64c0-c448-3363-9785-44e0695b8ca0 | -11.91112 | -46.40677 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 750c215e-3ae8-3520-b396-a640434ea5d5 | -13.36424 | -46.95327 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 75a84713-021f-3a31-b7f1-96e95a160d64 | -11.36333 | -43.54554 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 586fd8c2-9edb-32b5-82a4-99b9d994582a | -8.96323 | -50.00607 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59fb054f-7a2e-30ce-8ea6-414bcf6c7a67 | -11.88335 | -46.7071 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60f19ffe-c6cd-3106-a69c-0b667550dd13 | -10.75505 | -59.81256 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a195b493-3354-3d3b-a8c3-0d8cc891ddc1 | -8.67587 | -62.42697 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 191a0486-35e5-3fb9-bc9a-58128aecd61a | -9.06131 | -65.42474 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39af7b88-4ca7-360b-b8d3-223ccf025974 | -9.57819 | -54.49371 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f09c22-57a7-3bf5-8206-9a5a24e1e77c | -11.34744 | -43.62852 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f17304b-8800-3f78-9b9b-62e96a185ae8 | -11.07483 | -44.63133 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ca8b4982-a397-3f72-8ef5-52ba506ba598 | -11.01648 | -46.87473 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bf1128e-2188-3b39-a8fd-e5757855b7e6 | -10.31287 | -59.19595 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc616ab-844d-3243-959d-64d392f116a8 | -7.43761 | -50.26086 | 2025-08-31 04:51:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed616108-d7a0-331a-b7d6-153bba2034ad | -9.45548 | -62.35894 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f8dfeb8c-7ccc-3f7f-a312-8d4589060535 | -9.44501 | -62.35706 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0d39105-79f5-3977-bf44-b557b377ef37 | -11.32875 | -43.6638 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cddcd897-6cef-3da4-aca2-851a4e0ba325 | -12.63516 | -48.20295 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1df2fd9d-96fc-3385-855c-b3247c61c603 | -9.62261 | -47.80257 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ab5f192-7817-3bd8-8e7a-babfc65f381f | -9.07304 | -65.43256 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c796a4e-99cf-3bc1-9418-369c5e56e287 | -12.42298 | -63.91214 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37720613-99df-360c-a9c9-60631993a577 | -9.44037 | -62.35291 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb4ce6d2-b97b-32a8-a7ba-3441353e37e3 | -12.62131 | -57.01002 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47a3e8ef-ed5d-3142-83d0-756f8bbc1412 | -11.89818 | -46.46759 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5dc4b8bb-99c8-3083-96bd-028a1efb895f | -7.74771 | -50.26478 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d29d84e4-21a0-34df-9e5d-3cbb9ec2f09a | -13.6857 | -46.88214 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2fad8a1-c947-3cb7-adea-437e036c40b3 | -9.43831 | -60.55054 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70a75ece-8cfd-374e-9ec6-cbc1d8514b71 | -13.36373 | -54.38262 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0579b61d-0320-32e8-a626-24fc69c4f061 | -11.32944 | -43.63423 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4615aca4-e4fc-3252-baa1-4794d30e5284 | -13.35373 | -46.96091 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6065ecac-a2b8-31fe-b153-1ff9ee5825a4 | -10.60441 | -54.91509 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c5e9920-a379-3ee5-8361-99dd89fe3968 | -10.75433 | -59.81662 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb345ff9-bc1d-3cb9-98e2-390f3865ce8c | -7.91661 | -63.00745 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd2de17d-669c-34b4-b7cf-05bed2548ff0 | -7.73349 | -50.26329 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README66.md)
