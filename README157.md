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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cce238a-55bd-3b29-8f69-44ace1208e9c | -20.44752 | -48.83759 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 46f3f7ca-fc57-3dfe-8ead-90365d192743 | -20.26998 | -50.39454 | 2024-10-09 04:42:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6aafed7f-d2bd-34ab-8eb8-a581d295cd30 | -19.83457 | -50.34822 | 2024-10-09 04:42:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6fe3ec17-f627-309b-8da7-3b374a1cbf11 | -23.34775 | -53.91041 | 2024-10-09 04:42:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 592e2a1c-44fe-3f77-9d73-45e882778436 | -23.34714 | -53.91419 | 2024-10-09 04:42:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1f5ab158-6678-3cdd-8e38-bd1ad1b77a63 | -23.34441 | -53.90977 | 2024-10-09 04:42:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72d78d60-1038-3e39-b956-8c28abe55509 | -23.33834 | -53.90472 | 2024-10-09 04:42:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 04095860-cb63-30c2-bb74-39dfd2f6a72a | -21.6521 | -54.48881 | 2024-10-09 04:42:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 37f13d07-f3f3-3e61-a0f6-4d3e3b289510 | -22.28962 | -50.00455 | 2024-10-09 04:42:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cc8f0566-e30a-3737-a971-b87bdd754345 | -21.82532 | -49.16072 | 2024-10-09 04:42:00 | NPP-375D | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 685328b1-1696-3e89-a012-62f968d40486 | -21.28213 | -51.0448 | 2024-10-09 04:42:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1212d323-cb8a-3a03-857c-08605cd87900 | -21.27872 | -51.04422 | 2024-10-09 04:42:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2faf1158-2dc7-33b3-a25c-bba3c72d00db | -20.96308 | -49.34439 | 2024-10-09 04:42:00 | NPP-375D | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 54d0fa19-7df8-361a-8dfa-cc70934a162c | -20.87224 | -49.57118 | 2024-10-09 04:42:00 | NPP-375D | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2e83442a-24ad-37a2-ae8c-659b55d270b2 | -20.86864 | -49.57063 | 2024-10-09 04:42:00 | NPP-375D | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e48f127-75a2-3d13-b479-85fcb6e38661 | -20.5822 | -50.11968 | 2024-10-09 04:42:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49e6a182-5404-3616-978b-43e885f0e102 | -20.546 | -50.12221 | 2024-10-09 04:42:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 113d13f5-0850-394b-ada9-1a953760bcf1 | -20.45124 | -48.8381 | 2024-10-09 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bc6cb773-2e7b-3394-a650-7031b127f9a0 | -19.77497 | -50.13554 | 2024-10-09 04:42:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51326a9d-da3d-3a9d-b658-b8f25ffd0930 | -19.77439 | -50.13958 | 2024-10-09 04:42:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87e35ded-0357-3b4c-99c8-bf124fa8deeb | -20.01008 | -42.43919 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a1751d6c-c36f-3b67-8481-efb1037205ee | -20.00972 | -42.44263 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7dd4326e-fa1a-3260-8256-3dd308bae16e | -20.00936 | -42.4461 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ffb449f6-32f7-32e3-8a50-39052717e1ab | -20.0049 | -42.43515 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ce6966ec-b862-3677-ae12-4def7434c22d | -20.00451 | -42.43889 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| eb072ef4-8cf4-3f93-926b-20e867027bc3 | -20.00418 | -42.44217 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3dc01863-68bc-3390-95bb-6a29e1533b70 | -20.00384 | -42.44546 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 39adfa4b-4172-3480-95cc-7e5290b7a1d2 | -19.99938 | -42.43442 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3bdb3460-84e9-3d7e-b139-916be56880db | -19.99899 | -42.43823 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6f58cdc0-8486-3ab8-8db7-b4a1508ce721 | -19.99865 | -42.44155 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f282ace5-5ec6-3b23-8c94-50997b0b968e | -19.99832 | -42.44482 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 96f9673f-ea77-38f5-a26a-6662bd59b480 | -19.99386 | -42.43373 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47350d01-2cb7-3d05-b5e4-a4b9774edc0c | -19.99346 | -42.43762 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69109064-d22d-34c5-be2d-82312d4813a2 | -19.99036 | -42.18744 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dbecf794-143d-3266-8b31-245aa0998a8e | -19.99003 | -42.19078 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1b2f658e-9029-368d-99e7-81158b35a733 | -19.97615 | -42.44299 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a1785c42-186f-31a3-823c-f315c22bcdec | -19.97168 | -42.43181 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d7f86548-0157-3446-a954-e25bd825fd7e | -19.97134 | -42.4352 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 97c9a3e1-f8ce-358d-8b1b-cae1162870e0 | -19.971 | -42.43862 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ed25acfb-9452-3bda-b50b-766314ecce5f | -19.97065 | -42.44211 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 16ceb97c-9d55-3add-b19f-40cafcc89e18 | -19.97029 | -42.44569 | 2024-10-09 04:42:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5ef71275-169a-34e6-93c7-c5f057e0480f | -19.83264 | -42.38371 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 51a3e43a-e809-373e-a67f-4d4aee0c42dc | -19.83233 | -42.38668 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1f490560-07b8-3e52-8d4d-7a7ab7e61344 | -19.83154 | -42.38251 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dcda69ee-2ffd-3f57-93f8-7d44dcf5184a | -19.83125 | -42.38543 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4282a0a5-37fe-37de-8ffb-7bdc4f7a59d0 | -19.82708 | -42.38342 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 54aa17b0-e314-3fdd-8829-afad30fc6576 | -19.82676 | -42.38642 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6f935ac5-30d7-3204-94fa-72f80751b4b2 | -19.82599 | -42.38202 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9961fa33-19ac-326f-8638-0fd11bb73f44 | -19.82594 | -42.0643 | 2024-10-09 04:42:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2c8b6810-5661-32e2-8bb5-0bd2e4023d64 | -19.82569 | -42.38507 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6075b502-e94a-3b1a-9652-272d3d0bda83 | -19.82555 | -42.06824 | 2024-10-09 04:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d915c3cc-5cd0-302c-bf0d-79a40906c62f | -19.82156 | -42.38266 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b6ff4f0-8035-3a27-9452-0010686abe63 | -19.80251 | -42.4044 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5dc3cd53-5842-3038-9c6c-cb04bfada1b1 | -19.80213 | -42.4081 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43bbc376-0085-3911-b1d4-0d76e5fd9d56 | -19.79703 | -42.40334 | 2024-10-09 04:42:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d669c81e-fb5c-3d95-ab06-38dff397ff84 | -19.77024 | -42.33644 | 2024-10-09 04:42:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8bbf0696-ce05-3f4f-862f-17dee98c67b7 | -19.72783 | -42.21049 | 2024-10-09 04:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 11a3cd20-333d-3ac4-869b-35ffe2ea12a1 | -19.72743 | -42.21426 | 2024-10-09 04:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 787cc992-9bfc-3ccd-97d4-ca66081bdfb7 | -19.72647 | -42.20878 | 2024-10-09 04:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7bf6a2a1-d8ba-3df7-9681-03495e87ae53 | -19.72611 | -42.21252 | 2024-10-09 04:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 4649dc2f-fd7b-3a19-b853-95edca033d72 | -19.72188 | -42.21328 | 2024-10-09 04:42:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0bcd783d-7612-3dcd-9b01-84878af34422 | -19.89043 | -42.63549 | 2024-10-09 04:42:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4547dfd-7a68-3b0e-9fea-f53389a5fa73 | -19.89007 | -42.63925 | 2024-10-09 04:42:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d19d12f3-e2e7-301b-8a76-4f6b32a67d4e | -19.76998 | -42.83843 | 2024-10-09 04:42:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| efb310ae-47ee-3ac2-8420-cc6eabd8a470 | -19.76962 | -42.84208 | 2024-10-09 04:42:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ae99aae7-8504-3594-807c-721e833c7b00 | -19.76785 | -42.8392 | 2024-10-09 04:42:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3480162a-dc51-39b3-89a8-c405452189d5 | -19.76746 | -42.84279 | 2024-10-09 04:42:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8bd8b04e-61dd-318f-b4c1-1de1b57d6d1a | -24.62633 | -50.97599 | 2024-10-09 04:42:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2f818200-7e47-3fb3-acaa-acda8f85e9e7 | -24.62574 | -50.98022 | 2024-10-09 04:42:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 802b42ab-677a-30f1-96e1-b5f2f5b58d46 | -23.80852 | -52.06548 | 2024-10-09 04:42:00 | NPP-375D | QUINTA DO SOL | PARANÁ | Brasil | 4121109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd84c751-ad8a-3c98-90a4-7c4ec0a5ff99 | -23.37276 | -52.04478 | 2024-10-09 04:42:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e3e4016-3fbc-3ff0-9d50-2def62ed6a94 | -23.29137 | -52.12275 | 2024-10-09 04:42:00 | NPP-375D | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2f3d30f4-d8e7-3b68-b1a3-cbef3037b355 | -23.28406 | -52.12539 | 2024-10-09 04:42:00 | NPP-375D | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1b6b4d29-3b1c-3f76-b2f7-c7805d394713 | -23.20897 | -50.89632 | 2024-10-09 04:42:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d19142cb-43c1-3d03-9333-5613a619cf5b | -23.20549 | -50.89571 | 2024-10-09 04:42:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 80b27b1c-4152-3e79-810c-80b7f149a239 | -23.14921 | -49.79328 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| be6a4444-e896-374b-a029-c30835d6d6ef | -23.1492 | -49.82106 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14c3f8bc-5261-3ed3-b4bd-604ff59eb01a | -23.14862 | -49.79765 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d48eb604-eee1-3bc4-a9bf-f622b452219b | -23.14555 | -49.79284 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a501b8bf-082e-3c84-a43f-910b45bb05f6 | -23.14497 | -49.79714 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 588d509c-bb48-3d85-a08f-2dd31fb7e3bc | -23.13524 | -49.81421 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8c7667d5-6a32-381d-a485-a0bf6d71309c | -23.1346 | -49.81904 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2247c283-5a06-328f-8156-99e11063b27e | -23.13161 | -49.81351 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2bc96af4-b2a6-34c5-8321-629efa009b73 | -23.13097 | -49.81832 | 2024-10-09 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e856998e-0061-3212-aef3-a2bc31737648 | -22.86582 | -51.25468 | 2024-10-09 04:42:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dc7f4427-53cf-3fbd-8ceb-74c26a2c109d | -22.66001 | -50.94174 | 2024-10-09 04:42:00 | NPP-375D | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ab46fc2d-6202-3af4-812c-2cb53697389c | -17.75823 | -57.10807 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| af872d5d-933b-3873-b11f-dd137728deec | -17.75355 | -57.11092 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 51f4150d-cbdc-3124-bb59-b475a8ae1b95 | -17.7402 | -57.09311 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 35e615cf-7583-37ac-8009-0597294b98cf | -17.73953 | -57.09674 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 05a7c714-57d7-3a63-a06c-b01886ec6462 | -17.73619 | -57.0923 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8a8b7ce5-e44d-39be-a889-5dbb8bc48dc7 | -17.7349 | -57.07693 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5ef8dd1d-fb02-39e6-bf16-28cdf3f00046 | -17.73151 | -57.09513 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 32cdc622-0b41-3ab6-930b-3a68ce9b40ce | -17.73089 | -57.07613 | 2024-10-09 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 71eeaf50-0f94-3ce6-8982-a66d22aba170 | -1.11 | -53.6173 | 2024-10-09 04:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0842fce0-6e28-36b8-8c66-32d69558326d | -3.9208 | -46.4459 | 2024-10-09 04:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d57778f4-f6f1-3a30-aab5-77c71c0c0ea1 | -3.9023 | -46.4467 | 2024-10-09 04:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9f125041-7d23-397c-8216-61704c2ebcff | -6.7799 | -60.036 | 2024-10-09 04:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1b46799b-a8d2-3f29-9c5d-0cac7d6ab166 | -6.7798 | -60.0552 | 2024-10-09 04:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 6a09821b-3b40-3534-8b84-130243638da1 | -6.7615 | -60.0367 | 2024-10-09 04:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |


[Clique aqui para ver as próximas entradas](README158.md)
