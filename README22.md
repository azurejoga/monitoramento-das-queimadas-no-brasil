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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a15cafd-131b-3752-8cf8-4e2837863548 | -15.02548 | -50.09167 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eea3e44-86ed-3af4-8e37-a7e58613fa18 | -14.5879 | -48.02263 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c726821-5a19-3a51-9b1d-c6351e2ec50f | -19.23868 | -48.68084 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c16949c-14f8-30c2-9c8e-750ed836b016 | -15.03336 | -48.11415 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d01b1c-3bca-3537-9323-085f725cb653 | -19.21641 | -44.48643 | 2025-09-04 03:38:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b846a5ed-3034-3ac4-af6f-fcd101c4dfa9 | -14.81423 | -48.22498 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dcad6a8d-3ff7-3795-b1e0-04dd2677da19 | -15.0206 | -48.11143 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c4cbad5-ab22-325f-87d6-adc0cdf29a6b | -12.46256 | -48.08509 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b58fa126-dc16-34e5-b7e3-9ce7aa5551a2 | -12.8992 | -48.05168 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 195fa27f-47ed-3bcf-9763-b8ffa9d6516e | -14.54068 | -48.05559 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 591d64d3-f46b-3322-9d93-4774f525e655 | -14.28797 | -45.22912 | 2025-09-04 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47beda5e-4b3d-3c93-ba63-afb8d9b2f9c7 | -12.94111 | -48.07002 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ea49c19-cb17-349e-8ae4-68082e92b398 | -14.81903 | -48.23494 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9ccda67-e584-34bc-af2c-abcb7fc1f1ff | -18.32522 | -50.97697 | 2025-09-04 03:38:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| dfd9eb99-4540-3cf5-9ff0-068982bdae72 | -17.16776 | -46.25384 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9714ce2e-cbdf-3c56-945e-121d464ae21b | -12.86403 | -48.02239 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e11d9aa8-2344-3fbe-be2e-9deea94d08ea | -19.79216 | -43.34937 | 2025-09-04 03:38:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad85bbff-ca99-373c-be3f-b3166f886b31 | -12.50491 | -48.06525 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75e4dfb2-f61a-3d2d-ab60-2c1f7948e0ad | -17.05325 | -46.44253 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af1abca8-a317-3c33-a526-b8b901858859 | -13.45216 | -46.83749 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68a74dcf-13aa-3a14-b053-4c917ef79d53 | -19.25458 | -46.53326 | 2025-09-04 03:38:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc2fab1f-05f8-376f-a368-39d702ecca4f | -15.04444 | -50.07355 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e51e93ae-9468-3e5a-8a04-4cab5b726f68 | -17.05798 | -46.44766 | 2025-09-04 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fb0eb31-d3f1-30b3-a550-0a7b1ea53466 | -17.17766 | -46.26042 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 2c19bd7e-9079-3fc8-a466-c5054facc0a1 | -13.00079 | -48.08089 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 752ca2ae-1867-3c4d-b55f-1163e9c770ad | -20.09204 | -44.14068 | 2025-09-04 03:38:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 225b96d9-752d-3a2c-bbfa-9ecf7a0a59eb | -16.0762 | -43.6242 | 2025-09-04 03:38:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a96f01a5-a136-350b-bf96-7092cd23874b | -19.23741 | -48.68738 | 2025-09-04 03:38:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52b2a8c3-99c6-3556-8cab-b9817927290a | -13.73405 | -46.91746 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 30ec57a0-e16a-30b0-b439-3d7a90e5c25e | -17.9697 | -47.12423 | 2025-09-04 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b9cacf0-e3e9-31d3-8d1b-d623894910cb | -14.82156 | -48.34762 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 232ef543-5527-36e1-b395-95b9d7958f47 | -17.6114 | -46.64744 | 2025-09-04 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b0d306a-6a75-32bf-824e-c2747b0bfa77 | -17.16693 | -46.2301 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 917b660f-1021-3495-b40e-48e081798cc5 | -12.8994 | -48.03954 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60871acc-4ce1-3ae7-bd90-ca397b851a59 | -14.55779 | -48.0695 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba56e9c1-df00-3d74-bd2d-7f13af1e33c7 | -15.54943 | -48.38336 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa08aaef-075e-32f5-99c3-13a28436a5b6 | -14.19848 | -48.07878 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a878c763-63f3-3207-9ac5-216c60720ac9 | -14.81736 | -48.21172 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 27866041-9d72-35f4-a964-1d817bc38423 | -13.57327 | -48.13556 | 2025-09-04 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 090563b6-1bc3-37f6-a81d-a14d8d4d0a13 | -17.1576 | -46.24752 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc3de315-5814-36b9-93f4-f8a2898feeff | -15.1843 | -48.01553 | 2025-09-04 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2cd9b50-fc25-3e73-8d7f-cfa734138924 | -15.00075 | -50.03577 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bb6b20e-d9b0-3bb9-9328-544ab863a6c5 | -13.74165 | -46.94223 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3ee0d24-8102-3d5e-ae5e-47b6c1ad8770 | -12.8705 | -48.02435 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f64a4d92-3e45-3b6a-9343-2e4ab3c14cf8 | -14.7711 | -48.14364 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 138c691c-5f27-3a3b-bb32-c7cd063c2104 | -12.45874 | -48.08665 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 876a8ef3-ca29-3df2-8b62-90bb50d1ccfc | -19.47041 | -40.06377 | 2025-09-04 03:38:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 709a9d3c-a756-3ab6-acbb-d2cabc6825d1 | -17.17791 | -46.26017 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 57a1834f-140a-37b5-bd40-55bed2f7b851 | -18.68552 | -48.18338 | 2025-09-04 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e325706c-b2b8-3109-8816-9b7a047a7dab | -16.2966 | -45.69154 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 321a9ad6-97b6-3bbb-8405-26640ca78e76 | -17.15683 | -46.25127 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d8e97d2-8846-3f54-b72d-6d6f270649c7 | -14.82282 | -48.21622 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 178ddec2-4cfd-34a2-8386-fe00a7c4ad33 | -12.85712 | -48.0226 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75eb3b2b-1ae6-37f1-8134-d3eb5cf065e8 | -17.97347 | -41.92934 | 2025-09-04 03:38:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9af2bf8b-9954-360e-bb23-9438b766e14b | -14.74994 | -48.08644 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4f1d40-683c-3eb1-854d-b269d99753d4 | -13.44351 | -46.94199 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ff86b22f-f952-3323-a31d-94bf571e5c19 | -14.80777 | -48.22475 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f982a86-2a8b-3555-af00-31434302f77f | -12.94877 | -48.06635 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae5b219-9ff4-3973-be81-580e1489339b | -13.74293 | -46.93598 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a06ca7de-c0de-3a9d-abde-b921d0df1575 | -17.15214 | -46.24624 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e719ef71-ffc2-3255-93dd-03f4be2420a7 | -12.46008 | -48.08033 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59cdf96c-301a-37f4-8465-3321cb55a382 | -17.1738 | -46.25165 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7adeadc7-478d-3324-82eb-ae98ee10b11f | -12.46385 | -48.07882 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e540844-d7a9-3670-b81a-e903959fe62d | -15.04278 | -50.08099 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f128ce8c-31a1-3864-bf17-1ca59aec03f6 | -14.54186 | -48.05011 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b5413db-0d48-3418-bbad-9058c46ba115 | -16.00365 | -49.28429 | 2025-09-04 03:38:00 | NOAA-20 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3bc9697-de45-36aa-acff-4271bbbfddf6 | -15.53811 | -48.34031 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2144f44a-37bc-318a-bead-bfe72a33393b | -14.57193 | -48.03481 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b40c7703-bf43-3e0d-8823-66237658270d | -15.53699 | -48.34551 | 2025-09-04 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb8689f7-7df6-3495-9b2e-7d2b4e91b916 | -15.00785 | -50.03733 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb0325ae-8744-38b1-9e9b-2db654b827ed | -16.30584 | -45.7011 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e041d440-50e2-36eb-bf40-b5d984379393 | -14.33118 | -42.95405 | 2025-09-04 03:38:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 075b66ab-ef46-3dc8-ba07-67e0ccab871d | -14.78517 | -48.1406 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71cc7704-b480-3e6d-95cf-e4bb0eb78ae5 | -14.81609 | -48.21751 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3c6463c-90ff-3efd-9c24-772a0e4dec9c | -14.53946 | -48.06119 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f2ba20c8-f970-3c11-a31e-222c0c153648 | -15.18762 | -48.02127 | 2025-09-04 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3649baae-77da-3f18-a40a-8120288fd3a1 | -16.30877 | -45.70597 | 2025-09-04 03:38:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b89f003f-9be1-3e63-b867-37b837a71df4 | -13.85611 | -47.97684 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5da8269c-11c6-32c1-b949-4bee97f2d2b8 | -15.0364 | -48.10664 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24a0eed8-a01f-3134-83ab-335849557014 | -17.17698 | -46.23671 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8f28e6c-2718-3b37-9dab-6870ebe46534 | -17.173 | -46.2554 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f395d1a9-bef3-3469-81b5-c6fc4641a219 | -15.01161 | -50.03615 | 2025-09-04 03:38:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e85d0b8-b535-3a07-b1a1-be401fdf7a0d | -14.58638 | -48.02977 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a22bb11-5c10-3256-bb2f-57fe255b82e3 | -16.30197 | -45.69272 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae55ff71-9379-38df-b4cc-ced0c12f1ffd | -13.33913 | -46.83059 | 2025-09-04 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4984f644-8ae8-3f2b-b2e4-47a5ceb0596d | -14.59289 | -48.03057 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8926067c-e1c3-3ee6-b62b-9f53ee8f68c4 | -14.90316 | -49.63446 | 2025-09-04 03:38:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c023ed0b-b005-34c0-bd1f-5c5ca350366a | -13.70347 | -46.88161 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eff0dd4-81fe-3da8-8600-4b2997ace038 | -13.86264 | -47.97785 | 2025-09-04 03:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4618179-1a5a-3a73-899b-84ea1429ca96 | -15.04072 | -48.1109 | 2025-09-04 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c21ea1e-0e84-380b-8b08-9ecd051a5b4f | -12.46523 | -48.08881 | 2025-09-04 03:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49a80fad-bd61-3759-8c16-b2606834dcee | -16.30046 | -45.69991 | 2025-09-04 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52d8b000-4aa5-35c0-9251-bf6b37097736 | -13.74655 | -46.94927 | 2025-09-04 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 987db48d-fa03-325c-863b-6f3279d3aa80 | -17.97685 | -41.93405 | 2025-09-04 03:38:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7dfcf502-8a8c-3f3b-a15b-04e5f87d3ad3 | -20.09311 | -44.13524 | 2025-09-04 03:38:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01b7cc85-07ea-31e9-b45e-55c9f14a1275 | -17.1677 | -46.22636 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e93fe8e5-f50d-33b9-8656-a0c25ac45ac1 | -14.59551 | -48.01826 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0c1ac37-fe68-322a-816f-036f8ced1cb0 | -17.16686 | -46.23046 | 2025-09-04 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304adb05-d68b-3697-9848-94bc3e7a37b4 | -14.20509 | -48.07943 | 2025-09-04 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fad64af-f7f5-3d09-8eb5-bd0ab393fcd5 | -19.79648 | -43.3504 | 2025-09-04 03:38:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
