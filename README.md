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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12cca5dd-062f-3eab-9dbb-d9ea81923fe9 | -13.1496 | -56.8255 | 2025-05-17 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 78b04d59-b3b2-3b18-b757-685f5b39aa39 | -19.0711 | -53.4599 | 2025-05-17 00:00:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 9f3e886f-3dc1-3e20-ac49-9c8db981f708 | -13.1308 | -56.8071 | 2025-05-17 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1b631287-88cb-3056-a5d4-0f30e4f6e06a | -13.1498 | -56.8054 | 2025-05-17 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 136983ef-e54c-3a60-b16c-084b5894939b | -13.2977 | -45.3835 | 2025-05-17 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 182.6 |
| f95147ea-8fcc-36f5-aed0-b83248bef035 | -11.1722 | -48.6714 | 2025-05-17 00:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d8d3be95-6acb-3dc9-9c2e-9358c79b87ff | -13.317 | -45.3803 | 2025-05-17 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 8690c91b-29f6-34c5-93d7-366d0e6e1485 | -13.2981 | -45.3603 | 2025-05-17 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 2d0b0be2-3306-3111-9dcb-9a5ea483749e | -13.3175 | -45.3571 | 2025-05-17 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 9d77f559-f3fc-397f-b350-810b0ee52c04 | -13.1308 | -56.8071 | 2025-05-17 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7bf812ed-9b84-3c02-be44-823e7331e5f1 | -11.1531 | -48.6736 | 2025-05-17 00:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 6b163e18-cdf3-3985-8130-1327935623be | -11.1722 | -48.6714 | 2025-05-17 00:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8ca9c7e3-4601-3f64-92ee-669a2b494440 | -13.1498 | -56.8054 | 2025-05-17 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| fe9e0677-8fba-331e-8321-10f2261a77bb | -13.2977 | -45.3835 | 2025-05-17 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| b4e489d9-50fc-3bd7-a148-51d01f561752 | -23.3944 | -53.7203 | 2025-05-17 00:10:00 | GOES-19 | ICARAÍMA | PARANÁ | Brasil | 4109906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| 9f97126e-1fbc-3fe3-bd52-f2cf2f768495 | -13.3175 | -45.3571 | 2025-05-17 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a7aba01b-49ca-3d9b-ab3f-3d42b660e446 | -23.4154 | -53.716 | 2025-05-17 00:10:00 | GOES-19 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| d48d7570-52f1-35ed-b1f6-9d19dc64cca3 | -23.4148 | -53.7384 | 2025-05-17 00:10:00 | GOES-19 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 114710d2-9f4e-3473-a302-7fb40cd9ebe4 | -13.317 | -45.3803 | 2025-05-17 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 184dc2e8-a581-3d4b-91b2-cdd35e298842 | -23.3938 | -53.7426 | 2025-05-17 00:10:00 | GOES-19 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| 75b301b1-0648-39a4-962a-c0a5a32524ce | -13.2981 | -45.3603 | 2025-05-17 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 3367d7c2-316d-3fca-b035-858d51f2c688 | -11.1722 | -48.6714 | 2025-05-17 00:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 26162cfe-aad0-33e6-828e-f8b0f050d426 | -6.7051 | -42.1473 | 2025-05-17 00:20:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 2235b271-3d5c-33b2-bb68-6d7f2b2428ff | -6.7053 | -42.1234 | 2025-05-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| c0e024a8-0846-3a15-a657-6a874bd09ca7 | -13.2977 | -45.3835 | 2025-05-17 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 9b21a6f5-9995-3ae9-a487-7160a9335c2a | -13.2981 | -45.3603 | 2025-05-17 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 567887e9-47b5-3978-981a-10e243c56f23 | -11.1531 | -48.6736 | 2025-05-17 00:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 7e1a6f14-f41e-37e2-bf88-b5dd496a3778 | -13.317 | -45.3803 | 2025-05-17 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 98b82660-9cf3-33c2-a01d-7bbcd8cfb39c | -6.7239 | -42.1455 | 2025-05-17 00:20:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 81ec120c-5775-34ed-af62-5acf5030951c | -13.3175 | -45.3571 | 2025-05-17 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0f9efd60-740b-35cc-b4d2-14ec8aff4f20 | -16.2971 | -49.8912 | 2025-05-17 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8487002a-ae7c-3ab6-8ae2-e9d1fab65cef | -6.7242 | -42.1216 | 2025-05-17 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| a3d3e07b-ede2-3325-9cdf-fae3c8ea141f | -13.1498 | -56.8054 | 2025-05-17 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 357b9b00-ec08-39ee-8d83-8933b60d9eaf | -13.1308 | -56.8071 | 2025-05-17 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2f16acba-ab36-318f-9242-8dd5bce21699 | -16.3168 | -49.8879 | 2025-05-17 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 40d0af00-3eae-39d1-bb05-dd9c8aeb9bab | -13.317 | -45.3803 | 2025-05-17 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| f7547b2b-b13e-3e11-ade2-fe7de974ab08 | -13.2981 | -45.3603 | 2025-05-17 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 24813b11-9828-31df-9273-6b5a11844abe | -6.7053 | -42.1234 | 2025-05-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 89053496-c58a-34bf-8955-1bedacf186e3 | -19.0711 | -53.4599 | 2025-05-17 00:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 58ddd6f5-b577-34bc-8ae8-50915ca9f0ec | -13.3175 | -45.3571 | 2025-05-17 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 07c75dfc-7a87-3982-9577-1a43f5806aa3 | -13.1498 | -56.8054 | 2025-05-17 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| fc7061a4-b408-3a90-8516-08cd8f65d0db | -6.7239 | -42.1455 | 2025-05-17 00:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| dde2b8f4-b36d-3927-aa21-1db77b7d4e9a | -6.7242 | -42.1216 | 2025-05-17 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 186064be-4ea9-3edf-8411-14dfd4353932 | -16.2971 | -49.8912 | 2025-05-17 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9872f3bc-9172-39e3-a1c6-fcaef5e270a9 | -13.1308 | -56.8071 | 2025-05-17 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ecc47ce8-dbc4-3960-bc46-d96e6771811e | -13.2977 | -45.3835 | 2025-05-17 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 5ab7e1b4-1cb6-3942-b8c1-f107832af270 | -11.1722 | -48.6714 | 2025-05-17 00:30:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a44b0044-38ad-31c5-93fd-5e40faebc408 | -13.3175 | -45.3571 | 2025-05-17 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 471e9c3e-bb0f-38e1-a7f0-787e6bc16f1e | -13.2981 | -45.3603 | 2025-05-17 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 8461dab8-29a6-3e32-a667-049e8f706be5 | -13.2977 | -45.3835 | 2025-05-17 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 27dafa9d-1db4-354a-8c32-52bdcffd8233 | -6.7242 | -42.1216 | 2025-05-17 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 13d87435-1d49-3f6c-99f2-ebf69ed15f6a | -13.317 | -45.3803 | 2025-05-17 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| bade6617-aea3-32ba-9c13-f569739464a5 | -6.7051 | -42.1473 | 2025-05-17 00:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 99aa369c-a01f-35a9-8e34-8f1c911a711e | -6.7239 | -42.1455 | 2025-05-17 00:40:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 589e2270-b478-31ec-9443-e8ee6f6d3f23 | -11.1722 | -48.6714 | 2025-05-17 00:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| abcaa4bc-1272-31c9-b374-c5b203ba08e4 | -19.0711 | -53.4599 | 2025-05-17 00:40:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d9ceb369-49e3-3dc0-9bfb-9e56f795efc0 | -13.1498 | -56.8054 | 2025-05-17 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 87b48e87-aa89-3c9a-aab5-cada046fc36c | -13.1308 | -56.8071 | 2025-05-17 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 1ee6ccbf-b815-3ee1-9475-98a3a27a799d | -6.7053 | -42.1234 | 2025-05-17 00:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| d05df727-7ef2-3eb1-a7bd-a1add8784311 | -6.7239 | -42.1455 | 2025-05-17 00:50:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| cecbdcca-4877-36d3-936d-650eaccad94c | -13.1308 | -56.8071 | 2025-05-17 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5ce1c2a9-fd21-340d-ae3b-a21640f55eec | -11.1531 | -48.6736 | 2025-05-17 00:50:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 89fcddcc-ae26-3d10-b262-5238507577e7 | -6.7053 | -42.1234 | 2025-05-17 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| b32d165c-77cf-33e6-9d78-b4ebfd5f78be | -13.2977 | -45.3835 | 2025-05-17 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c3a39c37-a2e9-3c4f-9b91-bae5282ced6a | -13.1498 | -56.8054 | 2025-05-17 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 85159493-0d5d-3bca-b86a-f87e0a2d943a | -13.2981 | -45.3603 | 2025-05-17 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 99d9b822-0d43-387d-8864-174c82972267 | -6.7051 | -42.1473 | 2025-05-17 00:50:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 2424135f-0d1d-3d94-b131-584b53072700 | -6.7242 | -42.1216 | 2025-05-17 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 7db2de68-537c-3467-8327-f73c4606f1f3 | -13.317 | -45.3803 | 2025-05-17 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 4d5cbc93-f58a-364e-8f3b-afc08b450808 | -13.3175 | -45.3571 | 2025-05-17 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 0f41dc4f-3744-317e-a9dd-3934a20706f7 | -13.1498 | -56.8054 | 2025-05-17 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 66d4ca09-cea3-335b-97a3-ca168bf48f46 | -11.1531 | -48.6736 | 2025-05-17 01:00:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 33b55789-1561-32d0-b861-1c1907820d56 | -5.1053 | -44.8103 | 2025-05-17 01:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ae31257d-b011-3205-a917-b00db49dac45 | -13.3175 | -45.3571 | 2025-05-17 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6fa91c62-fa15-396f-bd03-b56940567dbf | -13.317 | -45.3803 | 2025-05-17 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c9f624b8-2e02-3c61-8aa5-a88dff007068 | -13.2981 | -45.3603 | 2025-05-17 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 635c3c22-a8cc-3e56-adc3-f9e62c58e9b0 | -13.2977 | -45.3835 | 2025-05-17 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| dd5b1bca-0831-35ab-b091-255b42dddab2 | -23.41008 | -53.73401 | 2025-05-17 01:09:00 | TERRA_M-M | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ef17b549-f7c4-3820-b392-691583efee95 | -23.4012 | -53.73548 | 2025-05-17 01:09:00 | TERRA_M-M | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 8f7f03d3-0cc6-3967-ae7b-1d773daaedae | -13.317 | -45.3803 | 2025-05-17 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 3215c72d-3666-3aa7-b398-6e07aaa71887 | -13.3175 | -45.3571 | 2025-05-17 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 42395203-676e-3b44-bc9f-293d6de37df4 | -13.2981 | -45.3603 | 2025-05-17 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7c03b18a-c042-3bcf-9013-37d3d096001c | -13.2977 | -45.3835 | 2025-05-17 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a4d1013d-a9a9-3487-bc70-5da50e57c387 | -13.1498 | -56.8054 | 2025-05-17 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| b9669113-1d38-30c7-a27a-2331732f5922 | -18.95632 | -52.23943 | 2025-05-17 01:11:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a4233e6e-c3e6-3b8a-9bbc-f9890ae01847 | -19.06127 | -53.45832 | 2025-05-17 01:11:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 41.3 |
| b30016fd-6979-3976-8a2d-1c9d68f53a19 | -18.95786 | -52.24961 | 2025-05-17 01:11:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 37d1516e-2501-30ae-9a4b-0ec34f4d17af | -20.95169 | -56.6056 | 2025-05-17 01:11:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 1ef26107-6b33-364f-bbd8-2c480bf72065 | -20.19443 | -55.06538 | 2025-05-17 01:11:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff915d25-31d1-333f-b297-415492df5596 | -19.07016 | -53.45687 | 2025-05-17 01:11:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 95ac4ddb-2f50-3165-9aae-bf3eb05be6a5 | -20.95308 | -56.6169 | 2025-05-17 01:11:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 095ca8e0-f30c-37d3-be20-ab653b90fb56 | -23.29413 | -55.30015 | 2025-05-17 01:11:00 | TERRA_M-M | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 5ab6ba03-bee8-3f85-b7e2-e896658b0abf | -13.1406 | -56.80318 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f0e79d12-8ee4-30cd-84aa-b3a5e6122f4d | -12.45738 | -57.20002 | 2025-05-17 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8166c2f2-b163-3af0-9aa3-0f23fbe878b4 | -13.14311 | -56.82202 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9a52a0f-01f4-381d-85e4-e2a2da36d316 | -13.31473 | -45.39051 | 2025-05-17 01:13:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 69aeab13-a561-3b49-a850-3abde7a738fc | -11.41281 | -54.32129 | 2025-05-17 01:13:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd44dfa0-807a-3136-869d-cee813805206 | -13.39411 | -56.90939 | 2025-05-17 01:13:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| bf12023b-3371-31bf-a1be-00e0a70427c0 | -13.85252 | -59.73136 | 2025-05-17 01:13:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 06a2a7c5-a336-3b7c-a037-6b2ed0a1388c | -12.64929 | -57.19017 | 2025-05-17 01:13:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |


[Clique aqui para ver as próximas entradas](README2.md)
