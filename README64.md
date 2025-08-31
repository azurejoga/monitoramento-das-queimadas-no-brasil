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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cd5f06e-01f1-3b06-bf1f-a46b9ed7b913 | -11.84105 | -51.49381 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 908e157f-f346-38b0-bd3a-3162a0ddd700 | -13.35015 | -46.97226 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e9d2150-a40b-305a-b458-18425582fdf0 | -12.56398 | -44.79787 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b5ed979-d793-39d2-a858-fa2dee543957 | -8.67117 | -62.42257 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c330712-1ae5-33d0-957a-bcddde47dfbb | -9.47022 | -60.3195 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47e8d24-932b-3f1c-8a2a-b71e47267cf6 | -9.69609 | -47.04692 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd96b680-bd14-3614-849f-475f5fb5b114 | -11.07082 | -44.74131 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ebb935a-7411-353f-87da-6bae73dca2ca | -10.61726 | -54.92089 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae321767-53bd-3299-8b80-ee59c4410929 | -11.36214 | -43.60278 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17c40eed-3326-30fa-a99b-2a1d763243f0 | -11.9045 | -46.68991 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cf167005-1bdb-3b53-a9d3-912636a19974 | -12.31127 | -45.72997 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5396748-d3c4-30cd-9d13-2a15dc1e2a39 | -8.85125 | -45.73483 | 2025-08-31 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 296ac598-14b6-358b-87b0-dc8a0408508c | -10.40777 | -64.52793 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3611c821-0ea8-34e2-b3ab-7160615eb0c3 | -12.42915 | -63.90966 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25a1a880-d241-319e-a35b-45b584da24a3 | -11.06988 | -52.05879 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6098bebe-e967-3eab-9fb4-aa5e2c9df3eb | -8.56021 | -63.02552 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 460f355b-d995-3892-ab30-c34387b95169 | -10.12817 | -58.01758 | 2025-08-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1411d6e0-606b-3768-b5a3-75a084995773 | -11.07837 | -52.04871 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c872cf-62ce-38eb-b340-ccb054e40f51 | -13.01308 | -56.88275 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1795c1b-c7bb-3beb-a53e-4e2a60c0abb6 | -9.68785 | -47.03963 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea9de40e-1f34-3f69-bc39-18b81de7bba6 | -9.43293 | -62.33473 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28edee0d-5c8c-3be1-8678-5229f1435e24 | -11.90512 | -46.68512 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efd22da3-0748-3367-b3b4-46ff88d9b2e7 | -10.09518 | -49.2872 | 2025-08-31 04:51:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707e95ff-ebd6-34c4-8107-ac7caf66476b | -11.33561 | -43.63091 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 650b886c-541a-3369-8edb-e85caba7cdae | -9.46422 | -62.34074 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bab3540-0877-33c8-950b-da10f6c905a0 | -11.41302 | -63.24854 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 372f2a26-33ff-39ee-a5c0-15df78ec0857 | -9.45782 | -62.34616 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b85f7bf1-7a71-30bb-85dd-782ee065175a | -9.30974 | -59.22041 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd5b15f2-2da5-33ec-afd3-e06a2d873d1c | -11.06253 | -44.64304 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51fe32ba-7280-35c1-be0e-e62882b447a8 | -8.34993 | -52.53558 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79762faf-6101-3aed-aab0-d83ccb838535 | -13.68647 | -46.89036 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9b2e14f4-00a0-35ec-94b4-24b63d56c179 | -7.94983 | -46.39319 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bea84b68-6933-39e6-8f68-02349aed4378 | -11.88025 | -46.73133 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8ba8711-b046-3ac4-bbf7-99244f47006e | -12.31703 | -45.72472 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad557202-9445-30ba-b46d-9ab932d19f98 | -10.60521 | -44.32927 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 73a1cb3b-6769-384c-9b54-32ea34894a78 | -8.74168 | -62.3875 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48638b10-bc28-34d5-be84-ded7b8ebb634 | -9.66931 | -63.17076 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d370818-e200-31b0-84a0-b63ffafc4bc5 | -8.56297 | -51.30625 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e807e7e8-1da8-3d3c-a6df-47837afff780 | -11.08402 | -52.03438 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ae07fae-9f7c-34d4-865d-ed405a3bdf3b | -11.82219 | -46.42218 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 809b8543-2902-3c73-9bf7-e21831661c95 | -13.02716 | -56.88523 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff8cb3c4-9121-38f9-b43e-72053c10eeee | -13.02026 | -56.90472 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c36cd51-37e7-34ca-951e-bbc97c8368d1 | -10.10737 | -49.28405 | 2025-08-31 04:51:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54c2a47b-f11b-3873-a9ab-14c25298bbc1 | -9.66219 | -48.34761 | 2025-08-31 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9146817-e927-3408-a3af-a814d9e6de9e | -6.87922 | -56.47104 | 2025-08-31 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df279cfb-6f15-30a5-83b4-25f92987f6af | -12.62774 | -48.19392 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60b7cd5b-1aca-3100-94b9-c90b1c426f56 | -12.5171 | -53.82877 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdbdf78c-30bd-3489-a0ad-03a03f5d88fd | -13.99022 | -46.3161 | 2025-08-31 04:51:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57457c19-d540-3cb2-9202-7e9cc154473b | -13.57579 | -46.91835 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce54b8c1-5218-3171-aa50-652c968a5f8d | -8.67772 | -62.41686 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38b9e9af-d6ad-331b-b302-29a8865bf11b | -9.06234 | -65.41948 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02261b35-0ea1-3105-8616-e4c7fd7ba05d | -9.60244 | -55.37928 | 2025-08-31 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 051bbba0-e864-3658-ab54-a4766c7b5e34 | -13.49021 | -46.93816 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 602944c5-de1b-306e-86e7-51aaf0d6ea0b | -10.59886 | -54.90676 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92e4b122-2b4c-3298-ab27-ebcb687cfc98 | -10.60027 | -44.32515 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df5f66e4-c9bc-3746-a577-8ed565cba1ea | -13.47561 | -46.94064 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aaddccc4-6605-3bcf-93f8-e690e8e87c45 | -14.99197 | -46.70729 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca779f4a-5633-36f0-a9da-408934538a0a | -14.98832 | -46.70941 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 595fad37-618a-3476-974d-04410a4d6686 | -11.314 | -43.68908 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf72fa33-cc9d-3a44-a5c4-b86dd2d5f9af | -12.30985 | -45.70148 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a783c567-42e0-3831-81da-2f028d839e27 | -7.73703 | -50.26381 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91074fd4-519e-3ed0-b8b4-a46daa524f25 | -7.73412 | -50.2591 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1628150a-5cad-37d3-af26-f6db9b3c8d2d | -13.46743 | -46.96799 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2759569-61e4-33a7-b376-fc927dde7d63 | -9.25298 | -47.06957 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 90d73ee4-70c9-39ac-8601-a030f30037a2 | -12.87088 | -48.08577 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7296cea1-a3c1-37ed-a636-ae5461a5e97f | -13.35138 | -46.96233 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c32fb04-5a28-30e1-bd03-e7cb225f5c98 | -8.65365 | -62.82789 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4de4d75a-10a0-3ef3-bbb5-533aa3b5d04f | -10.24013 | -54.97793 | 2025-08-31 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd297a00-4904-38f0-afa9-02ce8e67fe18 | -9.44845 | -62.36775 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e04edcd-3d03-39e6-b259-936677173d87 | -8.2975 | -46.31978 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1e1d43b-2697-3172-b1f5-7bef565c65a5 | -8.34537 | -47.41171 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cfa4869-a1b2-3aec-a7fc-15ebab0f1120 | -9.43857 | -60.57583 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 321642a2-d2ab-373f-a516-96bdb2a0c936 | -12.62194 | -57.01182 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5bbd51f-0d4b-33df-ba44-0327c9301d47 | -12.31523 | -45.69929 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b67b75f7-3cd8-3e84-b5d7-13ad5f4ce2c0 | -8.42959 | -62.29294 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 427cb637-c3b1-347e-aa54-3a75fe9f5478 | -8.74352 | -62.37763 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9089db7-198b-358d-be4c-80360a6cead2 | -14.63896 | -48.06501 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 482c1911-9407-396a-8215-70bb99477655 | -11.0113 | -46.95592 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2daa83de-dc39-3f3c-85bb-89c6d9462a0a | -12.55649 | -44.79676 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2e3fe12-c569-3e38-afdf-a11c805d125a | -8.41866 | -47.35016 | 2025-08-31 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2235a7f9-48e3-3500-8b76-bee46fd42f85 | -11.35311 | -43.62939 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6e3f257-876f-3773-bd03-e34079f0af29 | -12.80415 | -48.09424 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11ea2d1f-b7ba-379f-9526-395364df6553 | -7.92082 | -63.01608 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc45fa05-b1eb-3061-880c-a22f926206b0 | -7.9222 | -63.00851 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 267c2407-ee99-353b-870d-f865a0fcaabb | -8.64768 | -62.82731 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62bd4c34-ba18-3a8e-b015-d21c8ae27d6f | -9.44156 | -62.34645 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5ac5ed4-b6fd-3d85-9b55-783f2609696c | -11.34288 | -43.52248 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73751e40-ffd7-365e-93af-ffa8d414f012 | -11.83993 | -51.47752 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c65735cc-3901-383e-ab33-16dfad46b78d | -8.88757 | -45.09676 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be993f22-b007-3259-864d-3f2cfcae4703 | -12.81861 | -48.08411 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42db9637-89d8-3094-8cdc-535338c5e37e | -9.44965 | -62.36124 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 53a1dcec-55d6-32e8-8bd2-5db451bd4694 | -12.81269 | -48.09571 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bade235-ca77-3ec6-847c-f18b2ae35871 | -13.34909 | -46.96008 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3435d03-6a6b-380a-9f9d-fd1f045d9223 | -10.95736 | -50.85694 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0c536977-534f-3278-8be3-17915fa8a73c | -11.27638 | -63.23846 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0daa7835-6ce1-377d-86fc-abb25ecdd09c | -12.42845 | -63.9133 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2b3f9c-f793-3f76-ac48-0ebc2714dc7f | -13.35242 | -46.97078 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee71bc83-a33a-34ba-925b-29ae149d2594 | -9.45724 | -62.34933 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0a750e7e-673d-3244-9fa9-88bd5bc10bed | -13.47388 | -46.97048 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd1989bc-cb8a-3a5c-be7f-d36a1c4734b6 | -10.22537 | -51.11505 | 2025-08-31 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
