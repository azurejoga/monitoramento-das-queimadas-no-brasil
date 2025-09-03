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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbfc8a4d-ba30-3550-8fe1-33f9756e883a | -10.48429 | -53.64618 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a46970a1-7815-3fe7-84b0-85e8e360f66f | -9.3307 | -55.23019 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0dbb886f-86d7-33c4-9fa8-73d06984997e | -11.60797 | -52.09246 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| ccd4d6be-d1ca-37b2-823e-a298713b3e0c | -7.54151 | -47.45072 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6882cb2e-244f-3d72-9cf8-8590212a3c0b | -9.50935 | -48.90463 | 2025-09-03 00:50:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3962ba3f-2def-348e-87a4-c094938f3c1d | -10.95265 | -50.77497 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6381b373-e841-396f-8644-137ac84a7a13 | -13.511 | -47.02108 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7798478c-ff63-3067-b6d5-b116e0fcbd38 | -11.61168 | -52.11934 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2885d073-8de6-3ae8-a071-430459b46e85 | -16.29401 | -45.68756 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d5b2a942-21e4-38a5-9224-b4406659849d | -11.58644 | -52.13215 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d0fc1c79-84e8-35df-aca6-415b230d9841 | -12.44066 | -48.70935 | 2025-09-03 00:50:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 16ba9be2-b597-304d-9bfd-f5c7f15e66b1 | -9.74836 | -46.91229 | 2025-09-03 00:50:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| fcc5f76c-c76b-361f-babc-d61ca9618298 | -14.80724 | -48.22013 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c25d7963-035a-3282-b328-8bc12e20796d | -11.10629 | -44.65194 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3e7296ea-f203-3798-854f-ad9834855d5a | -11.61415 | -52.13726 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| a68b21a3-a841-31bd-b76b-d6af8ff564bc | -11.63816 | -52.11549 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 46b20302-72b1-388b-8d78-4fefe2943afc | -9.76529 | -50.02048 | 2025-09-03 00:50:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 28621d8c-ac2b-3910-94f6-878728428b73 | -9.32929 | -55.21928 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 84d06e94-d880-3431-be1a-7476608fafc7 | -14.34639 | -52.80414 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| bde797de-d417-3f34-82a7-1aa95b6d371f | -9.13919 | -49.65597 | 2025-09-03 00:50:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 43fe8c72-b023-3e5f-a6ab-657a49e28e1d | -10.08586 | -54.10308 | 2025-09-03 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad67ee4f-c578-3478-96d8-582a8788983f | -14.80545 | -48.20853 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2f28bacf-a124-31d7-b1cc-0f69b8c4f406 | -7.47328 | -44.82112 | 2025-09-03 00:50:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 35ffb6bb-cc8b-3ec2-9f92-f6a764e7f344 | -12.51082 | -49.5746 | 2025-09-03 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 36d40b6a-48cb-30d1-a010-1358e4529d2f | -15.15238 | -52.36277 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1c646c17-f5b3-397c-977c-610ca4fcaa88 | -11.85652 | -52.42928 | 2025-09-03 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 60242522-ec4e-3a8e-bc90-378c89c2a4b6 | -12.94908 | -56.98137 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 575369cf-5d25-38ae-b4b7-b3448fc4368b | -11.59914 | -52.09375 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9cfea7e7-3b98-38f3-a9b2-c3414077a4b8 | -16.82442 | -52.1398 | 2025-09-03 00:50:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 622bc29b-2cf7-38e6-a69b-09d015bf6a4f | -11.86312 | -51.47221 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b3fd19af-4142-3821-b739-2dc1bb1a307a | -12.99783 | -48.12022 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ded10f39-f503-3879-b1db-299f61cca192 | -13.27428 | -46.83793 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6560fb29-5fe2-3fe5-b6d9-98399c2363a2 | -10.46235 | -53.62046 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 415449a3-39e3-3c52-bf47-880572ec383e | -10.49147 | -50.33188 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8539c5b4-a8a5-3ce5-8543-45c959e2f2a9 | -16.5439 | -55.06993 | 2025-09-03 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 5d577160-c92f-3e50-8c4e-8a2d0d7fe78a | -12.48332 | -48.04617 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 52bf9dbd-308a-3a93-ad62-7571737f7185 | -18.02444 | -51.62111 | 2025-09-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 554791a5-c87e-3d58-a198-cf6e447d0f09 | -14.63092 | -48.94405 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 62627667-cc07-39dc-ad41-c3e5cbe08f13 | -11.39867 | -46.86144 | 2025-09-03 00:50:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7039e4ed-f1ae-3992-a254-f646adb2b6ff | -11.60656 | -52.14751 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1b498fa5-01b8-39b0-9e90-8cd1bd970e1e | -13.10701 | -57.14038 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3ba07a57-bf22-37a5-92d2-040bdf4d28ff | -11.85064 | -51.52591 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ed22ee31-1e3d-395d-9fdb-83b344f85295 | -10.47395 | -53.63801 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db3d27b1-0547-3eca-b15f-09fc9a53abdf | -10.48301 | -53.63674 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| dbfe643c-dc23-3ad5-9fc5-d6003cd879e3 | -11.8216 | -51.44742 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9e256f12-4a5d-325d-9f87-b3b6fa100077 | -11.61292 | -52.1283 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| eb6e5231-9962-31ca-8823-0deb7e4e9e86 | -10.97268 | -50.91478 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 21462e58-dacb-3e90-bade-a44df1e6b28f | -11.41549 | -55.18023 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 48622692-49e9-3060-866d-1950fe128a64 | -14.78863 | -47.5092 | 2025-09-03 00:50:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a976cd85-0270-355a-940d-e2240f0b189e | -11.87423 | -52.42672 | 2025-09-03 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6702b572-2062-3aca-a9ba-d8005f5d64dd | -7.94184 | -46.5399 | 2025-09-03 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 370ae26c-ab92-34d4-bf7e-e23bab2d68ae | -11.59156 | -52.10398 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 227.0 |
| 3a379cac-1ce2-3995-8fd2-00938491e8b7 | -8.88019 | -45.8258 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4cc5fbcb-4114-340c-bc61-9b20fe6e7a3b | -13.29662 | -46.83536 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 838f2532-a5fd-33d5-b09a-be085988a725 | -12.95102 | -56.99789 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ecce9100-4477-3829-a795-1e498d5141d2 | -11.59667 | -52.07584 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 623326ab-695b-36cd-b427-bcb8369b7b01 | -9.95024 | -51.63414 | 2025-09-03 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3a614bc6-18bc-3686-852d-59739a4d1e49 | -12.896 | -48.05732 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0126cc80-c61c-378a-a2c0-1426a42136e1 | -14.35545 | -52.80279 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0e2c44ce-f7c5-388e-a776-b6a14da51a01 | -14.56084 | -53.03766 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0169ec1b-f859-3766-b26e-5ffec47f2644 | -7.53901 | -47.43415 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d81166e7-d0c8-37e3-8a53-19f31eff0abb | -11.5319 | -54.41179 | 2025-09-03 00:50:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f6d8747-b82a-3c56-8d60-414ad19e35e9 | -11.64713 | -52.0502 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| db8bab56-6f81-3a3a-9e36-e57b94ba30ff | -13.51325 | -47.03514 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 59191d1d-537d-31a8-b79c-70a52c52d848 | -8.3612 | -48.29814 | 2025-09-03 00:50:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 004e0ba1-97ee-3dce-93fb-cd435fac090d | -11.5852 | -52.12319 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 625.2 |
| f082e104-bdf8-3ae4-81e2-e439ca77f053 | -11.61432 | -52.07326 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 6cd59fc6-a4c4-347d-b3af-27cd3eaaa2d8 | -12.8701 | -48.02464 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 86951395-80af-356d-8c50-72b61e045ea9 | -11.63692 | -52.10653 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ac5cd218-6b8d-3beb-921d-8028183630c7 | -14.56735 | -48.06494 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 46ad87fc-c2aa-3f2d-81a9-585e89dad69a | -11.58397 | -52.11423 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 688.9 |
| 42a7cbc5-4615-3a87-9676-69f87b40bfda | -10.07507 | -54.77742 | 2025-09-03 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 14435feb-fd6c-3d81-b3f6-03f04eb61567 | -11.19154 | -55.02612 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| af458da2-ac21-3e56-bf20-ea061ae57edf | -15.74336 | -53.66618 | 2025-09-03 00:50:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 20858d42-5e0a-38b7-ac70-6e11185c07d3 | -7.70318 | -48.7499 | 2025-09-03 00:50:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8b01df6f-c9ba-3e7b-a1d9-544a8b10cb34 | -10.47267 | -53.62857 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 19635ee5-1508-34fd-b3e0-af67e68960f8 | -7.62868 | -46.55072 | 2025-09-03 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9ac70ffa-d5c6-37ef-b491-3d1382a12fed | -9.33899 | -55.21803 | 2025-09-03 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4c91a518-17ed-35bd-8a50-017c1295534c | -12.63232 | -56.99612 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b786f52a-f2f1-308e-88cd-1b30eebb521f | -10.71672 | -51.5829 | 2025-09-03 00:50:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 44a7c6af-dfc0-31c0-bc30-63a1ada1701d | -11.62314 | -52.07198 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7b1d22c3-9d46-319f-be0e-c907e18b9344 | -11.19989 | -55.01368 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bacab519-377a-3fb1-83e1-5b8bf58d2167 | -11.60533 | -52.13855 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 1d1c489e-3165-3230-8072-1498eddb8d0f | -14.61159 | -48.0168 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b08cc69-15c3-3d75-b633-9fdbf9a216e0 | -8.37408 | -48.31011 | 2025-09-03 00:50:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| abc55c21-375e-326e-9d90-e9c857d1a302 | -16.866 | -49.58115 | 2025-09-03 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1251da51-04c1-37c9-8e84-f8cb13dc683b | -9.95785 | -51.62388 | 2025-09-03 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5354088d-8045-376d-ac94-7eb70de2ac71 | -8.06097 | -45.35992 | 2025-09-03 00:50:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 6f9a9d21-9d58-319f-a459-04f13ead7f00 | -13.20938 | -51.81255 | 2025-09-03 00:50:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| abd3ca55-e398-3007-8480-058d897cf8e8 | -15.08 | -51.35125 | 2025-09-03 00:50:00 | TERRA_M-M | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| efc3f8a6-9fe0-3855-a448-9f0ce6f75263 | -11.86413 | -52.41896 | 2025-09-03 00:50:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0605c27d-651c-3673-a79e-1dabac2d9e56 | -11.84666 | -51.41941 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 99409455-c6f9-3091-b55c-2a2c2c09d197 | -15.5798 | -54.32359 | 2025-09-03 00:50:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b78acfe9-83e1-3338-9c08-d3e3d9bbdf93 | -14.57 | -53.03637 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d61a7e6-d605-3f48-9c72-b85489591920 | -10.47715 | -50.35036 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d1ae7d3a-889b-3348-a088-8faa285b8471 | -14.5634 | -53.05733 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc6319f5-3735-3b44-b18b-2c7e380aacad | -14.60334 | -48.02942 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 925f64b2-992a-3be8-830f-da14a055e497 | -11.1901 | -55.01505 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 1bd7c7db-14a4-3f7a-bbc2-596fd1702505 | -15.55365 | -48.39982 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 265fa8b1-81f5-3a2c-8467-24dd81f66401 | -11.85552 | -51.41814 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README14.md)
