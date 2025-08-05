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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bc49d1b-2b69-3279-af08-0291804dbfa5 | -13.05567 | -56.87642 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c70a8b9e-86e2-3a0c-9369-2f1fbe06d383 | -11.76089 | -44.96626 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 352c7229-cd5b-3c1d-b9c8-a11ce5e5a974 | -13.18339 | -44.16825 | 2025-08-05 04:40:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 945d24a4-cb9f-3cfc-9001-9592705794f5 | -12.71457 | -47.79522 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2679151f-01e0-3fc3-99f7-046fed4dd50d | -10.46516 | -44.38659 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31129886-0d18-3b9a-a553-f7132b0586c8 | -11.916 | -44.96502 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741d0e72-aab6-3598-8c08-0bc96511a77b | -13.0724 | -56.87968 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32a217fa-bf10-3507-8c37-f3d3ed30a619 | -13.08413 | -56.91041 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c537fa55-ddf7-358d-96e8-0d1f188aa651 | -10.46721 | -44.38772 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a6bc18d-621d-315c-8910-6731a1ebec92 | -9.61936 | -48.49123 | 2025-08-05 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75a158d2-b3c0-3d3e-8c17-3d2d5fa23024 | -12.68476 | -48.0773 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c93f3950-481c-3aaa-a8cd-280ae0d108c7 | -13.00627 | -55.97459 | 2025-08-05 04:40:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c82a3d40-6438-386b-93ff-9dde8cf11b15 | -10.92581 | -48.36856 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a528e7f-8ebc-30f3-b586-68f95ba7ea27 | -11.76822 | -44.97553 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50e8a63b-0eff-3942-9e75-5265d6e3e1db | -13.03957 | -56.91493 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4daa99ac-2a5e-392c-8052-ae972bc71ac2 | -10.90852 | -48.36588 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66ae4cb3-9a83-34fd-b043-329b21ecc0ec | -13.04171 | -56.87843 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b6466c2-b835-34f4-9d31-62d6285dd4aa | -9.98693 | -49.29821 | 2025-08-05 04:40:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05562f15-65c3-32e1-941f-5445934a4725 | -11.74602 | -45.01155 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c268d6dc-0722-3e77-aee3-bc0f568a5fcf | -11.75391 | -45.01665 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0f7fdad-2955-3504-865b-266a99bb6ba3 | -13.0515 | -56.87202 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2a040ad0-1ebc-3178-94bd-82d7e3b07cd2 | -11.71908 | -47.7753 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32317d50-30bf-33de-af3f-decb310e310e | -12.54283 | -44.72675 | 2025-08-05 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b484162d-7c60-3d50-b780-73c4846a3164 | -12.51887 | -47.18663 | 2025-08-05 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72462c25-f955-3da2-bed7-3ef63fc62580 | -9.62276 | -48.49175 | 2025-08-05 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a237502-0c3b-365a-9351-dedcf1d3b0ae | -11.01182 | -47.18395 | 2025-08-05 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67ac26e6-122b-3c3c-856f-7aa48e9ca9c7 | -11.91878 | -44.97643 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3a708ae-e431-3184-b515-fec0a968c115 | -11.78715 | -44.99416 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfcdbdb3-8fa8-3eb7-8599-887833006131 | -11.92531 | -44.92776 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e11e8c9-2758-37f1-8bad-442950c931f9 | -11.91818 | -44.94876 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9858107c-5112-30af-ae97-a37e025bd327 | -12.67815 | -48.12271 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6634b63-5016-31a7-a04a-b0e3abc32061 | -10.77742 | -46.64558 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b6a8e45-ef76-3835-88b6-74c6f203b949 | -11.91874 | -44.94455 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d43446b0-97cf-3896-b244-42bcd60024ae | -11.81186 | -44.26543 | 2025-08-05 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb250e06-0cf5-370c-98c0-216bd900f173 | -12.71819 | -47.79575 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b00b8d2b-6b71-35cb-8f9d-604a5417031d | -11.78609 | -45.00174 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64ac99bc-e18a-3924-a271-7c5116bae562 | -11.74806 | -47.53927 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 438a5459-db76-3b54-9bfd-0b162b2ef16c | -11.74342 | -44.99927 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c9f848b-eddd-315a-82f0-fcf3497cb477 | -12.68881 | -48.12431 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb1cf4e4-6876-33d2-9290-082cf6e39be8 | -11.93406 | -44.95926 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85d6d789-9cbe-35af-ba6d-2f0cb8e02ff8 | -11.91548 | -44.96888 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e0c57d6-450e-3cb9-be51-92479dda349d | -13.05849 | -56.88146 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6c96d0d-bf6f-379b-b4a6-59afe70471de | -10.80527 | -46.50816 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e86bf655-021b-3ec6-9729-75a23e034503 | -9.77413 | -49.7533 | 2025-08-05 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9647e7bd-dd93-3b81-95db-6b317460078a | -11.78576 | -45.00448 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc955aa6-1f79-3aaa-99ea-d3ddb46acef9 | -10.11718 | -45.65118 | 2025-08-05 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f91d8a60-ab36-33f6-848c-6ddadcb64c91 | -10.47378 | -44.37241 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59b8f269-30a1-3351-8f78-78d4f61ceab5 | -10.92293 | -48.36414 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e0283d8-dbc4-378d-bf98-c5220fd8770a | -11.91653 | -44.96109 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4c59e4a-c710-355c-b144-1d34038f0b13 | -12.43179 | -48.70865 | 2025-08-05 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28c87f72-c381-3183-ab07-f16767f031ad | -11.74747 | -47.54333 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c3ff692-2a86-31cc-bd96-f932803186ef | -11.92357 | -44.94075 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56226bc6-a329-39f0-b2d8-6f79bde9b897 | -14.37512 | -50.32784 | 2025-08-05 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ac4086b-d06d-31fa-a8b4-1709e12aed4a | -11.7504 | -47.54082 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| de294673-233c-39e1-af90-433a5625240b | -14.05548 | -41.99139 | 2025-08-05 04:40:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ab6c3d9-13b3-389a-ad8a-f52d75d4944c | -20.74127 | -49.40275 | 2025-08-05 04:42:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76851dfe-c790-3618-bf5e-df744fcc6069 | -17.36069 | -46.09108 | 2025-08-05 04:42:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e7fc055-d1bc-3e53-9532-506b3125b080 | -17.68443 | -46.64554 | 2025-08-05 04:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9652180-c2f0-3947-88c2-8f5d941754c5 | -17.68546 | -46.6377 | 2025-08-05 04:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3e70ab9-c60d-37fe-be3a-f82c00cdcf38 | -17.68853 | -46.6462 | 2025-08-05 04:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09ad25b0-8241-3b6d-a333-953dc9f4057f | -20.74492 | -49.40331 | 2025-08-05 04:42:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec37d3c7-3449-30ea-aa16-ba24cdf0545f | -17.36118 | -46.08719 | 2025-08-05 04:42:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08ed3129-093d-3a1b-bfaa-ea884f030cab | -23.72207 | -47.46024 | 2025-08-05 04:44:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1b14bb00-322d-323a-b46f-33cddeb4896f | -23.65694 | -47.47036 | 2025-08-05 04:44:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 667f76fa-d212-3ffc-bbc6-eb7b2d834294 | -23.72237 | -47.46312 | 2025-08-05 04:44:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cd0361ab-bc12-3343-8737-08070a7eadbc | -8.9478 | -46.7354 | 2025-08-05 04:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| af60493c-ae88-3232-9c51-0857db8d6faf | -15.7872 | -49.9523 | 2025-08-05 04:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 2bf03893-2304-32fd-bd06-1db22e6b87c7 | -13.0538 | -56.8746 | 2025-08-05 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c9110cae-5a8a-347a-85e1-71b6a8b6cc9c | -13.0916 | -56.8913 | 2025-08-05 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3f1a55fe-4d8c-3ebc-b7a5-a0dffd9785c5 | -8.9225 | -60.576 | 2025-08-05 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e17e33ca-9da9-35ed-ac50-f142c989c650 | -8.9227 | -60.5568 | 2025-08-05 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ed02f7cc-10de-3ce4-ba3e-06a5f44234b2 | -13.0726 | -56.893 | 2025-08-05 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5854b01d-28c3-318e-9633-593c4cb283c9 | -13.0914 | -56.9114 | 2025-08-05 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c5b62d95-7baf-3d5e-a081-6ee499eca071 | -13.0728 | -56.8729 | 2025-08-05 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5a68d84f-e563-3578-bd1c-6929a9319b31 | -15.7676 | -49.9555 | 2025-08-05 04:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 17bb0698-8f8f-3b1d-8dd4-0543fe8d38f2 | -7.994 | -43.1534 | 2025-08-05 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 0cf8cb94-d687-3900-86c4-f52c23dd305f | -13.0723 | -56.9131 | 2025-08-05 04:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5cf7c081-8dd9-3923-890b-141a91cd994b | -8.9227 | -60.5568 | 2025-08-05 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 11533af5-83ef-3209-84c4-054415d0f415 | -8.9478 | -46.7354 | 2025-08-05 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 346241ef-70a5-3569-8313-94d5c93267fd | -7.994 | -43.1534 | 2025-08-05 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| a8df7572-38a1-32dc-b9ff-b6ccfee0aed0 | -13.0723 | -56.9131 | 2025-08-05 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 317608fa-033c-3c14-aa27-0709d013832b | -13.0914 | -56.9114 | 2025-08-05 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3d942cad-09f4-349b-8c7b-dfed9df63869 | -8.9478 | -46.7354 | 2025-08-05 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 57762ec2-00d2-3936-bcf0-54fb39ad879d | -7.994 | -43.1534 | 2025-08-05 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| ccf31bfe-dbd2-3e12-807c-8e4185bf857c | -17.2056 | -44.8214 | 2025-08-05 05:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c418c742-cb5c-3ca4-9ae4-ac45eb1c5ba2 | -13.0723 | -56.9131 | 2025-08-05 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 58ae3680-63c5-3d0b-ae0a-e7da0f566519 | -17.2256 | -44.817 | 2025-08-05 05:20:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 88fc9d27-6627-34a1-9734-3936d2b7d4f7 | -13.0914 | -56.9114 | 2025-08-05 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1d27ba5e-157e-355b-95d7-702525e53039 | -7.994 | -43.1534 | 2025-08-05 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| d2ec72a7-2a3b-3286-bedc-e196f4fc659f | -8.9478 | -46.7354 | 2025-08-05 05:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| c9b8f6a8-2322-3d2f-88d8-6cd7186f2fe7 | -13.0538 | -56.8746 | 2025-08-05 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8151f27d-588a-3685-a423-cc7b6f94acca | -14.2748 | -51.9874 | 2025-08-05 05:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c31e99fc-2a65-37bf-9a6f-8902fab2c0e0 | -3.88304 | -54.21291 | 2025-08-05 05:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c93ae7-82d9-387c-8091-2f78e0bf0af5 | -3.88799 | -54.24519 | 2025-08-05 05:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acae905f-5cf6-3d6f-86b4-4a339f6ce8be | -3.17012 | -59.1184 | 2025-08-05 05:27:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e54d860-3a2b-37c3-9cb0-52d4e71e9226 | -2.98193 | -54.49856 | 2025-08-05 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eba10598-f1d7-389b-8704-5971f7a01445 | -2.98578 | -54.5043 | 2025-08-05 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 108a6ca9-bdf6-39e4-9347-969f172bfe57 | 1.10371 | -60.58578 | 2025-08-05 05:27:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d57e02d-a517-352b-902d-af0d386492e8 | -2.98654 | -54.49932 | 2025-08-05 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166066ef-53ee-35bd-94af-ea0297bfd8d4 | -2.89725 | -54.1544 | 2025-08-05 05:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
