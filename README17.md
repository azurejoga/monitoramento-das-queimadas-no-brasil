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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f0f0f59-8378-35c1-b3e4-0019842515b0 | -15.20716 | -43.8218 | 2025-09-09 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1acf9f0e-2d3a-3bc7-924b-86c1e85f5106 | -17.28164 | -46.69417 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac92b181-b6ec-3b16-91f1-60ba71ed0cb1 | -14.54537 | -48.76807 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3228d806-15db-378c-ac35-88d9cdc843b8 | -18.73913 | -40.0861 | 2025-09-09 03:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0158cc03-f097-3c99-a5e4-24cd0ed35030 | -14.78782 | -48.23699 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94b5f932-5487-381c-9126-d4c8b9c004c3 | -14.79586 | -48.18896 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 641c8082-1f9b-3ca3-a5be-22aec2021384 | -17.80155 | -47.62209 | 2025-09-09 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c818e4d3-8cb0-33d9-868a-f90ec845bad8 | -13.79085 | -46.27787 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f785a12a-39ac-3674-9169-3f928fd44146 | -13.73551 | -46.89589 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2af4d73-c86f-3cf5-9709-37845d9cc4f8 | -11.64524 | -46.63127 | 2025-09-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bac0b751-ffff-3325-8833-e414ec5c3150 | -15.823 | -48.95208 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36a808a0-ed06-324a-afe7-8e3e1be7a63d | -11.33684 | -46.56637 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03e67e34-1497-316c-aa61-5df57631d040 | -16.90155 | -45.81573 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93d73863-9fef-3cfb-a040-606f352de190 | -13.84234 | -46.24003 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96e2ddb0-33ec-39e2-8367-cf9229ce1986 | -14.54652 | -48.76254 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db5af7b1-697b-38f0-9625-eab84fd2f045 | -18.3489 | -43.92263 | 2025-09-09 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50dd06e7-480f-3b02-9a79-ebff3ce83214 | -18.01762 | -47.13029 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b77aeadb-3d5d-3fe8-bf58-2dabc0edb019 | -16.89808 | -45.83284 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61659505-171c-35a5-a73e-42e77e64664a | -11.83464 | -46.75454 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19e7a360-c547-392b-9f30-54bc664a4a36 | -13.04534 | -48.03114 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e15424a3-87f8-3060-b111-73d23ca8388b | -11.29997 | -46.48462 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7050a80-af27-384d-93e5-b116bfd50391 | -17.56818 | -44.36031 | 2025-09-09 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 541d7bc5-5123-3915-a3a2-6d82ae2edea2 | -14.53132 | -48.74392 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 147d5b2a-111c-35ea-a994-81d41c1d8ebc | -14.32087 | -47.32226 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05094df6-6c1d-3964-9a7d-320067e26d16 | -11.83391 | -46.75832 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bdd99c3-fb06-3f73-960e-bd8b931c533c | -17.27556 | -46.74932 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cea80a0-e347-307c-9835-7593d2ec851c | -14.52612 | -48.73838 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 689b9d8e-cad3-3fa0-9c39-9653979a05e6 | -13.58692 | -43.56759 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55a79e8e-dace-3ed8-9b95-adb0664374cf | -14.53648 | -48.74963 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7ba5d7f-d75b-3907-a9d1-85c36062dd3a | -13.18599 | -47.2466 | 2025-09-09 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 949ea76a-1df8-39b1-8f59-fa9d86cff39e | -19.45466 | -43.93962 | 2025-09-09 03:45:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3382f95b-a402-3b9a-a309-b9a666463a82 | -13.58247 | -43.56672 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4391e67-2c72-39a4-a514-c874ec6b463a | -18.14905 | -43.39325 | 2025-09-09 03:45:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeed2172-8de0-381a-9565-0ff2e8a9a7ea | -15.66843 | -48.19276 | 2025-09-09 03:45:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca265402-8a7b-36c2-9a36-5fe92d73427f | -17.15675 | -44.44944 | 2025-09-09 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f23d5ee8-4fee-39bc-9679-3a9cf4e25a19 | -17.27111 | -46.74502 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 896b9d49-5e7f-3e1a-a9f3-77ea273c3be5 | -14.3377 | -47.30888 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f676fce-fe1f-3a15-94f8-699e9ec1d30d | -16.62928 | -49.14389 | 2025-09-09 03:45:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c2bdcb3-da08-326c-a691-7e79b01d2ef4 | -17.28666 | -46.69564 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bac6e119-1a43-3129-8b36-45d20a252e2d | -13.279 | -43.74819 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e289fb3c-0ad4-3c95-aaf6-93949873c1c8 | -11.33754 | -46.56268 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d92b7f7e-fa9b-3d95-98af-90c4063562de | -19.52205 | -43.98976 | 2025-09-09 03:45:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c21d786-4089-3bb6-aa39-ba8004f51302 | -15.52265 | -48.40577 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b86ca92-d601-3249-a440-84c9ca905f5f | -13.28384 | -43.75204 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0164b0a3-256f-3e24-8b07-1fd3866a5dd7 | -15.52811 | -48.39929 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92ebf4d9-297b-330b-873e-7810bfb7ac30 | -17.28913 | -46.70943 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b189d567-26cc-3b60-899e-7f98fa5038d2 | -11.30824 | -46.50221 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f58dab0f-2c5f-33ee-bc82-61d5e6423846 | -16.89554 | -45.82041 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ed2140c-4fc8-34cf-b61d-d1177dde027f | -17.28229 | -46.69106 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2825d74-dfad-379a-963c-fd620ff4b152 | -13.7511 | -46.90414 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8f75896-e3f7-382a-8811-f68b427e7042 | -11.82628 | -46.77895 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad9d13a9-2056-3f64-ac57-7546308c0429 | -13.74504 | -46.90576 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b0fdb24-6dc7-30cf-bbf0-da6397ef13fa | -18.76375 | -47.10366 | 2025-09-09 03:45:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f46407db-cf9f-3d3b-b0e7-93d991ad0f0d | -17.56946 | -44.54482 | 2025-09-09 03:45:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 46e0ea91-3ef0-3055-b8bf-7bec7834184a | -14.89842 | -41.45361 | 2025-09-09 03:45:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d5fe1775-c6b4-39c7-b562-4fcc53bc1549 | -17.08054 | -49.23544 | 2025-09-09 03:45:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a5f5631-6078-3e26-b2eb-4bb9b691e062 | -13.81481 | -46.24039 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89485747-9e5e-3b75-9c34-70ebd53d3308 | -11.84015 | -46.76844 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e588ac1f-291c-3cf9-8c31-cf621f4580a4 | -13.93757 | -48.22864 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bfa3558-978d-36c1-b4cd-126ec8d05eb7 | -18.0326 | -47.13613 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62084912-c837-3f2a-a9ae-c0c9c8f1f57f | -14.786 | -48.23556 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e36ba0c-76b3-3264-8fe8-da5381702ee4 | -14.33589 | -47.33446 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5a0bac2-3b54-39ef-8ebd-932166855616 | -19.45877 | -43.94044 | 2025-09-09 03:45:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 395a8646-b7a3-31da-a033-adc0e3f4d3d0 | -16.96343 | -49.68478 | 2025-09-09 03:45:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 43d76e44-c86f-3f34-8d61-2aa1ea58ef8f | -15.82271 | -48.95829 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82848339-5ef1-3cee-bf74-0d6e99fe6601 | -13.93745 | -48.24072 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6400c495-828f-3ee0-b843-5f7f02036097 | -13.74579 | -46.89866 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fca072bf-1ceb-3725-9196-321d2bfe0c89 | -13.65055 | -46.975 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4004426b-fbf3-3e82-9773-6688c4b0e985 | -16.28442 | -45.68662 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a031d9ec-690a-36fa-9e53-f737cfe69dcc | -17.286 | -46.69881 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9301c35c-1a78-35a2-af62-44517c13f533 | -15.52915 | -48.39439 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a605b7a2-db7f-3c40-80e2-7e48a99e7979 | -14.607 | -43.92791 | 2025-09-09 03:45:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13db0043-76c7-3773-ad90-591938da8477 | -14.76717 | -47.7816 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3196877-d52b-36ca-a50a-dbbde7f46221 | -16.29224 | -45.68712 | 2025-09-09 03:45:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc7adc76-8737-372a-b703-34d8ed2a9a6b | -17.72693 | -44.47861 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c35ff8f5-c5ee-386b-905c-f09e70093b4e | -17.15583 | -44.45435 | 2025-09-09 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50261d14-11a3-3f36-beb7-47a6a94a42cb | -17.25847 | -46.69129 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62033301-2c0f-3b44-b9f3-c69951523bd8 | -16.9574 | -49.6899 | 2025-09-09 03:45:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c94ddd0c-e95e-301e-9934-44dd85cb16eb | -14.67478 | -48.19074 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b8b2b6a-edfb-339e-946b-b42f3cf2e139 | -13.82008 | -46.2415 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2437e5b-67d8-3c99-80e8-2f83473efc5d | -16.69538 | -48.63341 | 2025-09-09 03:45:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 370d6338-993b-31e4-9dde-e000d1bcfa21 | -12.5126 | -45.2967 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df8d3e03-7649-3dd4-926e-82073e188395 | -17.29598 | -46.75387 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06c712ce-bc9b-3913-a255-c72222eac87c | -14.53744 | -48.74505 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad777fe3-9919-33a7-a342-369ad3807a2d | -13.27931 | -43.75116 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99fc02f5-2ad8-3ed2-b73e-79c3ec9780dc | -14.29571 | -44.89214 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58e92610-9f7a-3641-b06f-613fbb28825a | -12.15053 | -49.07959 | 2025-09-09 03:45:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6187d6d1-a232-32da-b3c1-6dfd8b8d654f | -16.89473 | -45.76019 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16a442fc-81f4-315f-949a-f4795f5797ec | -17.1533 | -44.44339 | 2025-09-09 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec12e6c2-3e20-3e28-bfca-81b43fe23c4c | -13.15842 | -40.68255 | 2025-09-09 03:45:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a06c10f-64a8-3edc-86eb-4dabd0fc1921 | -15.52654 | -48.38684 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a66829d-0b33-36e8-9ae3-812dbbd989fe | -12.52964 | -45.26242 | 2025-09-09 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83c8cd76-b01c-33a6-b4ae-92034bdf4071 | -15.44069 | -39.00486 | 2025-09-09 03:45:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a4cf8fb8-e5f6-3181-9050-fe20282ae849 | -17.15235 | -44.44841 | 2025-09-09 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 353575d9-83be-3fc0-87c5-4bae1dbd2ea4 | -15.52706 | -48.40422 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e47cd9c4-3c14-3533-b7c4-0ef8ee25ab70 | -16.43854 | -49.29064 | 2025-09-09 03:45:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b519571-e945-3b3f-ab49-7fa80e7d8f4d | -17.29617 | -46.72701 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64de9334-e2b2-3a3f-b36d-6b60bcd74b18 | -13.741 | -46.89713 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c7e4cc3-5939-3efb-8796-49a9d4e3bc36 | -13.47584 | -43.5053 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e76fc8c-ea9b-3ac4-8e4a-5a4ef398ff2d | -13.80561 | -46.28675 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)
