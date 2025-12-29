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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b61d5e7-3e3b-343f-8e08-3784f06d3c9c | -11.54978 | -46.31393 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae7ef193-ecf5-37fa-bd00-a0b8981bcffd | -11.54635 | -46.30283 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d3cf409-f3c0-33bf-a9d2-22848bd45a92 | -11.75438 | -44.5925 | 2025-12-29 04:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e0794ded-e2cd-3962-a129-2598b6424d0d | -20.42188 | -57.97126 | 2025-12-29 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 37627777-630a-377a-9672-9245bce3e4cb | -18.73158 | -48.02857 | 2025-12-29 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 84b32bac-6785-3707-b009-dd7af9f809f2 | -20.42529 | -57.97191 | 2025-12-29 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 61a8add3-5b3e-3f79-b160-e8f87ab3bc7f | -18.73686 | -48.02406 | 2025-12-29 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9efc6577-b622-35dc-a743-b5c1c14ba222 | -18.73627 | -48.02925 | 2025-12-29 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f3a50ecc-da7a-327e-ac12-44229205afee | -11.55593 | -46.30383 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 716ad0bd-fa4a-30fa-9699-7912ba134c3d | -20.42123 | -57.97519 | 2025-12-29 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7079c0d3-5819-3ef2-9cfd-173e68980527 | -19.85861 | -57.95343 | 2025-12-29 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 14829b6f-08a7-3247-b4cb-e32cc7fed7f1 | -19.86137 | -57.95801 | 2025-12-29 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8236a52f-7f97-3b4d-9051-d200136798e7 | -11.54568 | -46.30806 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96df2c24-0c83-3d7d-a3e7-35db784ebe2a | -11.96307 | -44.20987 | 2025-12-29 04:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61ff781d-8a4a-3a4a-bbe4-cd0014779593 | -17.29694 | -41.82136 | 2025-12-29 04:55:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d68169d6-7c1f-3b42-b51a-20e7e7b4559f | -17.29821 | -41.82489 | 2025-12-29 04:55:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 66de821c-0285-3f75-b914-3db583949115 | -19.86203 | -57.95407 | 2025-12-29 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| f73fa4ed-906a-339f-9651-eb362abfc62a | -11.7548 | -44.58905 | 2025-12-29 04:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6c54e53c-d509-3ec1-8f41-129dbb65b4c9 | -11.55112 | -46.30348 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83090122-0fd1-3444-9527-3e6bf562cb34 | -11.55729 | -46.29333 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13fa4e2d-0013-30a7-ba6e-d827a20ad13b | -11.67126 | -44.881 | 2025-12-29 04:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a2af792-9c8f-3444-ba3e-96d315d854b4 | -17.61276 | -46.66131 | 2025-12-29 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98a54c3f-ddc3-31b7-8e10-53bdc0009f26 | -11.55045 | -46.3087 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c5a5319-4a19-380c-b6cb-97eb0f0fe200 | -20.62417 | -48.93991 | 2025-12-29 04:55:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 02338dda-c0c8-3a86-a505-fd53d74a5651 | -20.62535 | -48.94111 | 2025-12-29 04:55:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 330898cd-ef0b-3908-9477-0eaa59a4dae4 | -26.98516 | -51.07876 | 2025-12-29 04:57:00 | NOAA-21 | VIDEIRA | SANTA CATARINA | Brasil | 4219309 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cdeb7342-1701-3d71-bf12-3f19b2b54436 | -6.5631 | -51.1126 | 2025-12-29 05:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d18242b1-f7d0-3317-abb9-1e97f9d75241 | -1.62434 | -54.21547 | 2025-12-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b365530-5231-331d-96fd-4640e76e25ee | -1.53415 | -54.52142 | 2025-12-29 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcabf90a-6342-33b6-9b84-4ff14914ea75 | 3.71006 | -60.87503 | 2025-12-29 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f1696c-7450-3934-96bb-e3256b0f9a94 | 1.83849 | -60.86791 | 2025-12-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 659c1f35-5fcd-35ca-8cfc-c237a4b680dd | -2.44972 | -47.78115 | 2025-12-29 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cc01c78-3697-323f-b316-7930005dcc61 | -2.01192 | -54.44915 | 2025-12-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a5031f-a95e-3955-b8e7-4c5b14201156 | -2.44914 | -47.78498 | 2025-12-29 05:20:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36f74415-484a-3078-b9d0-af6d58de3592 | -0.08875 | -51.27802 | 2025-12-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5475add-180e-371b-bb26-993f685b9c18 | 3.66441 | -61.07194 | 2025-12-29 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ccd4072-1cc4-3577-80e6-56338ea44a28 | -1.31676 | -53.48323 | 2025-12-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a637ddee-fcbb-3a0c-9c7b-4b09905bb50c | -1.61988 | -54.21935 | 2025-12-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 884721ed-42a7-30bc-960b-45d218488e92 | -1.62059 | -54.21489 | 2025-12-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d4d833-0a10-37d8-b87b-f024ada500ed | 3.66515 | -61.06995 | 2025-12-29 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db3e2c1f-77cf-3e7b-9c4c-d66a72854e24 | -1.53046 | -54.52088 | 2025-12-29 05:20:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25798f08-8d52-35d5-8add-b6d8c43aa21f | -11.55069 | -46.3093 | 2025-12-29 05:22:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a8c10bc-c93a-32ef-bf62-10a97b43b958 | -7.70465 | -55.20969 | 2025-12-29 05:22:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a82575e-3320-3329-9035-6629d7435810 | -6.21649 | -55.65349 | 2025-12-29 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 087b332a-7fa5-3cd9-9ce5-1551a07c7436 | -7.70849 | -55.21027 | 2025-12-29 05:22:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e249ccb4-bbd2-3d4a-bcbd-2f18b7c3b994 | -11.54852 | -46.31173 | 2025-12-29 05:22:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1661670a-fcee-3d7a-8135-845e09964131 | -4.43997 | -55.94431 | 2025-12-29 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe3c78de-273a-369c-a776-c41285c38797 | -3.59327 | -53.23596 | 2025-12-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abd439c9-486e-3324-b061-432f40f143b4 | -11.54349 | -46.30851 | 2025-12-29 05:22:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd951cf3-568c-3429-9bbf-58e6fc193d2e | -3.79277 | -54.40695 | 2025-12-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d8cf45e-99c9-3273-8dc5-90936858279c | -11.54933 | -46.30457 | 2025-12-29 05:22:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ba0f87c-32cb-3bce-9577-de7c02c1ca47 | -11.55146 | -46.30212 | 2025-12-29 05:22:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cae90c74-f594-3ae7-9278-b8dc04e1d002 | -14.50099 | -52.56017 | 2025-12-29 05:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59d3bb24-a9d5-31e7-a890-807c66c4f6ec | -15.45679 | -51.95686 | 2025-12-29 05:25:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 183a3a2a-ae29-3aef-8d3e-f9116cc54c7f | -15.4554 | -51.95617 | 2025-12-29 05:25:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2eb74d5f-f4e9-3a78-a7b3-1ce61fea462f | -12.30066 | -57.36452 | 2025-12-29 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c8cf0d9d-e13f-313f-a6d2-f6542154cf32 | -14.50605 | -52.56065 | 2025-12-29 05:25:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 000c9170-5b72-3bba-8c8c-cd799bae259a | -15.46072 | -51.95685 | 2025-12-29 05:25:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da2e6360-4ff0-370a-a263-41e354a95672 | -19.8572 | -57.95389 | 2025-12-29 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 32fac15f-716a-3a64-8352-9f3cbf8b2224 | -19.86102 | -57.95446 | 2025-12-29 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 190df9b3-547a-3f76-bd1e-d82ffa1c36ca | -20.42278 | -57.97118 | 2025-12-29 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 60cfe6bb-3d2c-3bc9-b78b-cd73b0b74811 | -16.59336 | -58.21021 | 2025-12-29 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 19305718-ccd3-3aa4-af50-bdee6041b30a | -19.85785 | -57.94894 | 2025-12-29 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4b6213e2-867a-3a1e-aab6-9c605a6acb1a | 1.83674 | -60.87037 | 2025-12-29 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed03847f-8d42-3a55-adff-563f938fc5af | 1.84027 | -60.8698 | 2025-12-29 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 913142dd-95cb-3442-8ccf-b5f67c206391 | -9.13693 | -61.52039 | 2025-12-29 05:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d70d333-264c-3b3b-841b-c1ae9e887bc5 | -20.42285 | -57.97273 | 2025-12-29 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4e94808e-c2f4-310c-a650-574500f29cbb | -19.85583 | -57.95335 | 2025-12-29 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 397fb9e4-e622-3bd3-8cbe-b8b67a94ea8a | -19.86115 | -57.95813 | 2025-12-29 05:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 39012e3a-4c2d-3752-97e4-3425d1f04da2 | -6.5631 | -51.1126 | 2025-12-29 06:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e001e701-db15-3c1d-9f1b-d1991d516c33 | -7.703 | -55.20962 | 2025-12-29 06:39:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3b00fa1c-9b73-38bf-861b-1616a87895e4 | -7.70433 | -55.2008 | 2025-12-29 06:39:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2918b9e-9595-3f41-a082-c16c21e3d0eb | -6.5631 | -51.1126 | 2025-12-29 07:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| bca419be-2d50-369b-aa95-0532f04eb948 | -9.08689 | -37.76107 | 2025-12-29 11:17:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 13.4 |
| ac82e7df-cd14-3158-8683-dcb1ad1a436e | -10.49031 | -36.67091 | 2025-12-29 11:17:00 | TERRA_M-M | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| fe4dc6c5-f82c-3e43-9cd4-63b63539118c | -6.17656 | -38.25275 | 2025-12-29 11:17:00 | TERRA_M-M | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 19.4 |
| f7eca95d-65fa-3f5b-8000-888a17bb34eb | -8.21463 | -36.6936 | 2025-12-29 11:17:00 | TERRA_M-M | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 7bff0863-a6fd-3b52-9562-6cda5398b3be | -5.86267 | -38.35096 | 2025-12-29 11:17:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 2d9505a1-b0a0-33a2-a945-b9065d1acbeb | -7.98137 | -37.61609 | 2025-12-29 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 2817d7c9-28d4-3491-8498-1d69ccacbf3c | -8.21303 | -36.70411 | 2025-12-29 11:17:00 | TERRA_M-M | POÇÃO | PERNAMBUCO | Brasil | 2611200 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| c7de8b2c-b977-3bbf-ad4f-e4fab2101365 | -5.65868 | -35.53103 | 2025-12-29 11:17:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 05c8cc82-d977-3992-912a-3b8cc2738cd4 | -1.48211 | -54.19786 | 2025-12-29 12:55:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c0f27427-eeb8-35d4-8a3f-d7905a534d8c | -9.8388 | -43.942 | 2025-12-29 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ccf1ca3d-7b5b-3cc2-bb0c-684cfa51a5f4 | -8.4752 | -38.5623 | 2025-12-29 14:10:00 | GOES-19 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 74ead22b-e959-3cdd-a7cd-4e41ff2555c6 | -12.6745 | -46.7605 | 2025-12-29 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| f8a5ae9b-7a26-32f1-a4e5-669b472d227a | -7.6752 | -37.2446 | 2025-12-29 14:20:00 | GOES-19 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 0974f55e-3288-366c-83ba-bf72927db644 | -12.8031 | -43.0923 | 2025-12-29 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 8a824a55-3ddb-3754-8215-df000f39d4eb | -15.4773 | -43.6608 | 2025-12-29 14:20:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 99.7 |
| e8211345-3089-36a3-83f4-aae157114065 | -12.6745 | -46.7605 | 2025-12-29 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 8046b315-6047-3584-b702-22de2cb00555 | -12.6553 | -46.7633 | 2025-12-29 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 85efa666-b5fd-39e1-b6cb-a25772d2ae47 | -13.411 | -42.7185 | 2025-12-29 14:20:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 5dacebf1-1037-3172-9f71-281c23f35db1 | -12.6553 | -46.7633 | 2025-12-29 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 1803c91f-6deb-3410-9bfb-e7b7d4339272 | -2.9003 | -42.1659 | 2025-12-29 14:30:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 5d2f2bc1-efa6-366f-9a7d-cbbc83947d98 | -19.3497 | -40.8888 | 2025-12-29 14:30:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 126.8 |
| 64286bdd-0672-3743-81a3-77cf483fbadb | -19.3497 | -40.8888 | 2025-12-29 14:40:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 121.8 |
| 50945258-71d2-3c68-9072-0fdc682c799c | -12.6553 | -46.7633 | 2025-12-29 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |


