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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac90ddac-be21-3afb-9f6b-cd124cb718b1 | -11.05452 | -62.5809 | 2026-10-04 05:18:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 266f6d1c-13fe-34e5-a402-b8b6c93410ec | -8.89485 | -66.88523 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9894c76e-ae24-3350-84fe-c7f822702d79 | -8.88281 | -66.89268 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b4c84d8-f086-347f-8c3d-a64e8a49cb1a | -9.21342 | -57.63665 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e12d141-33bb-31eb-a9a8-9b70ef6bf49d | -11.17514 | -58.16124 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21704abd-3814-3817-b2d0-86e03a9ba3c1 | -9.48503 | -64.69522 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5376b86b-e0c6-321d-b3b1-f99a2f487094 | -10.14103 | -61.74262 | 2026-10-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42c8abcc-9c16-3399-8668-36af98011398 | -6.0751 | -57.8053 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffdece27-4117-3fe5-b7b5-c557f95b36c2 | -8.70127 | -66.73327 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c538670-88df-39a3-b54d-2fd2b90bb64d | -9.08891 | -61.16929 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25550698-aa16-3a94-8fef-b79b376ecd01 | -6.07272 | -57.60655 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 185dfbc9-9221-33a2-a6c7-3fa8ddcdb0c1 | -8.51733 | -67.11574 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2992c1e-c0fc-3f2c-95f5-a751d36d9d11 | -9.91591 | -65.04305 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42786656-1847-3048-b0c9-2ef51c0d92a8 | -9.08381 | -61.15574 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 759d5333-7816-3f43-bb41-e789d5594a15 | -9.46852 | -64.33076 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 031f9021-09c0-37be-bf03-8c8b0733a2a1 | -8.8834 | -66.88951 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25d3bd74-6889-33d0-92db-e03c0088430a | -8.51675 | -67.11902 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a2fc5fd-2070-3f13-9f1d-33970a75de79 | -9.15337 | -68.27208 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dd450d0-51c5-33f3-a584-6b890f6db8a1 | -8.51149 | -67.11802 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e94b74a1-52c4-3b5f-9d7b-70236c26a477 | -10.65716 | -63.51817 | 2026-10-04 05:18:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc4f011f-e849-313a-be06-a94b1cee76ba | -8.33732 | -62.86774 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70ac9e44-3277-3531-92b6-431cfa18278c | -9.91306 | -65.0332 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1a33d49-f235-35e1-bbcb-9960ed7138be | -10.83552 | -57.20615 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a1c455-0fd1-33dd-9b49-cc033576fc47 | -12.18171 | -57.10682 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4ad3445-9e31-3191-a3df-f2dab9b11e4b | -12.17831 | -57.10628 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2e14e8b-cc8a-36da-98aa-c7e9bbdef165 | -12.1019 | -57.17117 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb72f9c-3f02-3e5d-9775-f9123bedf798 | -15.91077 | -56.34396 | 2026-10-04 05:21:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ee8f7ac-89b9-396a-afce-b7370704ddc2 | -15.91442 | -56.34452 | 2026-10-04 05:21:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ace67ecf-9671-3d4f-a0a2-832fdda57495 | -12.20442 | -57.11805 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc2f46f-ece2-3b1b-bc9a-b2c244adc87e | -12.20783 | -57.11857 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f52a5c9e-fdf8-3fd3-93a1-29a37474df9b | -12.19704 | -57.12074 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f5b9776-4836-3a1e-aa7d-ef6de2c33f69 | -12.13005 | -63.17107 | 2026-10-04 05:21:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f6c573d-1d01-3253-ab21-91278de02fe5 | -12.19534 | -57.10897 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bfd9820-4eed-375d-a14d-3bf2c794113d | -12.13387 | -63.17176 | 2026-10-04 05:21:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7102b21d-0010-3112-8808-bbbd70a59c04 | -14.5432 | -59.75857 | 2026-10-04 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 437aa74c-bc89-3ee8-a79c-dd035846ed1d | -12.15479 | -60.74886 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f18dd46f-7b09-3596-b6df-4743c3802f55 | -12.15944 | -60.74197 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba8d5a1a-c8ee-3a02-8c75-43ab26b96c00 | -12.10473 | -57.17542 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 102a050e-def5-3626-8483-98cb63b4a101 | -16.17817 | -59.12331 | 2026-10-04 05:21:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 80dd843d-1ea2-31c9-b447-3e092b86d04b | -12.19024 | -57.11966 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9149b8f8-6b18-33d6-8290-a95a706e111d | -12.17775 | -57.11001 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91c00255-3af6-34a0-93ed-f29e81446e32 | -14.56825 | -52.8805 | 2026-10-04 05:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45727f77-4a10-3fb5-b1c5-875ac0b10fd2 | -12.81677 | -60.49697 | 2026-10-04 05:21:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45de1ab9-2c71-30ec-a3ed-123e3bb3f1df | -13.50198 | -61.13374 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3acefa3-efb0-390a-aeab-2cd239e4501d | -12.55336 | -54.95243 | 2026-10-04 05:21:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7c42b11-5f19-37e4-b581-189f897afc85 | -12.19307 | -57.12394 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f05aadb-1ee2-3ce2-a94c-7c671a692b4f | -12.10246 | -57.16747 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf1bab91-bc00-340f-bcdf-2708f4399803 | -12.89116 | -61.72144 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff30053-aa8c-301a-ace7-6fa70c8f8c74 | -12.75792 | -62.08268 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5d1a59da-dee2-3384-b779-f93532a55c00 | -12.18909 | -57.10416 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79d484b4-5262-33bf-b157-8ef4bb03d651 | -12.77207 | -62.04227 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a63a7da7-7ea1-3951-a9c8-85a1f1871a93 | -12.76849 | -62.04164 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac1822e4-e0d6-3e50-a1c4-7ae75207fa70 | -12.77137 | -62.04643 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b012b826-273a-3ad5-ad1b-15ce561c4c73 | -14.57269 | -52.88102 | 2026-10-04 05:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b792245-1efc-358f-a57e-73b5fa347dd4 | -15.91806 | -56.34507 | 2026-10-04 05:21:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c52aab02-c265-37c4-b8ef-df3025152ba4 | -14.32537 | -59.5693 | 2026-10-04 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc34fee-a461-357b-9adf-94bb32b7bb2e | -14.54652 | -59.75912 | 2026-10-04 05:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd86fcf6-8f2c-3568-9f40-a6ed78ebd9b6 | -12.10134 | -57.17487 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f17e56-286e-3086-9787-a2031a6acc61 | -12.88696 | -61.72484 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d70c0651-524c-3067-84ca-52e3daa0ba0d | -12.19364 | -57.1202 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baa01cac-eff4-3939-901f-6bc193b7d16b | -12.19818 | -57.11324 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c52cedba-af6a-356e-ab25-f3430be31144 | -12.19249 | -57.10469 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee04e506-ce0b-33a9-a952-24750d1396e7 | -12.15819 | -60.74947 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17dd1f68-1ba7-36c4-8bda-6af2826c6bb2 | -12.18227 | -57.10308 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35388b68-d648-364e-b268-868c1fdbd6dc | -12.1448 | -61.17143 | 2026-10-04 05:21:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bb69258-71a9-3795-90db-4960ed76cc89 | -12.19874 | -57.1095 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f6d089-f4ec-3471-9fc7-3ec7c4b0b143 | -12.10586 | -57.168 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e19672f-5bb2-38b5-ac85-9052da8c141d | -12.88413 | -61.7202 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f41ea738-9725-3f62-a948-fb1af43e9420 | -12.19761 | -57.11699 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40121f19-d1c2-3dbb-868d-870b505c8532 | -12.77067 | -62.05059 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c83e019-2724-3992-9fc1-a30b9aeb9ecd | -12.13304 | -63.17659 | 2026-10-04 05:21:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93776451-8578-3400-841e-57ef2df78d9a | -12.91897 | -62.17711 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce36c740-48e1-31e7-aa6a-de7ba72a90a1 | -12.88764 | -61.72082 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cb10dbd-28dc-3c6c-b92a-ce7446ad6fe9 | -12.18967 | -57.12339 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d4c4df6-4477-3e63-8fe9-35e0d6812c23 | -12.19648 | -57.12449 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a53f3b57-3bbe-3a1f-a0a5-60fa0f9d5aa2 | -12.20385 | -57.1218 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d7652fc-b7c9-321a-bb15-892b61bb30ef | -12.17887 | -57.10255 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2898251c-229a-3a64-b6c2-c5a0b63674ea | -12.15882 | -60.74572 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce3c29e4-2c7c-3d96-a6c5-28cf6af4b6ee | -12.14416 | -61.17531 | 2026-10-04 05:21:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df18b984-6681-31c6-93af-222aa6d577dd | -12.77276 | -62.03811 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 328bb7e0-a32c-38b1-a94c-bd8336a0c539 | -12.1347 | -63.16695 | 2026-10-04 05:21:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1db809b8-3817-3176-a01a-deb8d04f8012 | -12.20045 | -57.12127 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fca2b9d-5dcd-3c05-ad9c-836e21753bed | -10.49342 | -68.03066 | 2026-10-04 05:21:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47b9e77e-7fcb-31d3-bb75-af3fe0a504ee | -12.18568 | -57.10363 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ab5080d-5fc5-3a5f-a3f7-e609a8807c8b | -16.7588 | -53.37875 | 2026-10-04 05:21:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f31521b-b75b-37c3-82f6-712e64b224ce | -12.91539 | -62.17647 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0faa1df5-0c88-3fc6-8cc0-54c3b11c65dc | -15.91744 | -56.34943 | 2026-10-04 05:21:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3027bff9-9576-333d-b1a5-c224b8abe714 | -15.99454 | -55.35286 | 2026-10-04 05:21:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08c1a794-88ac-3ee1-a688-34112733166f | -12.1959 | -57.10523 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c3d0c5a-c7b0-3a0f-956c-1cd132d8bdaf | -12.81736 | -60.4933 | 2026-10-04 05:21:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6706b5f0-5fb6-3827-8855-2841e67daea0 | -12.20102 | -57.11752 | 2026-10-04 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff27d4b2-427a-3a15-83c0-d5929477701b | -12.13687 | -63.17728 | 2026-10-04 05:21:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e519900-5ee9-367f-8f5f-b5d5cce8eb60 | -12.76919 | -62.03748 | 2026-10-04 05:21:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a1a44a9-1d77-3c8e-9ae1-340488acd9a9 | -13.50539 | -61.13433 | 2026-10-04 05:21:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88379765-430e-3bcd-a7a4-8e70ee67db7c | -12.14069 | -63.17797 | 2026-10-04 05:21:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b8178f-a2b4-3934-8306-bf32515d4854 | -20.22613 | -57.98907 | 2026-10-04 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 441e927e-71cf-3149-9870-3b1cac763609 | -20.23553 | -57.99916 | 2026-10-04 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 127f4edf-d451-3e6c-978b-994cd41e14f5 | -20.22553 | -57.99326 | 2026-10-04 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9255997c-caf6-342b-87e4-5315c6d45d80 | -20.23199 | -57.99859 | 2026-10-04 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 665cc787-6290-3e21-ac24-a52172a4037e | -20.22966 | -57.98962 | 2026-10-04 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |


[Clique aqui para ver as próximas entradas](README67.md)
