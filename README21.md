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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226a3b47-9e3c-3324-9961-d20024f31c89 | -9.20459 | -45.33243 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f6a8c85-a23c-3f09-94b5-bf2e56474c1e | -7.6222 | -44.93303 | 2025-08-16 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 203ce6b9-f5a1-3c2c-8b99-24d032656fe9 | -13.58379 | -46.97025 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cc723a7-e1ec-3de0-87bc-ba2706b2085a | -12.56364 | -46.96481 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 4a922a1a-23bf-3d1e-8026-ed40513c1c11 | -12.6184 | -46.94278 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6385ef67-08ad-3921-b165-98b457ef3d42 | -12.54357 | -46.94873 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3c00b335-c4a0-3009-a0ee-9417543f8c18 | -13.58229 | -46.97684 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fc88b7b-212f-30de-8633-39cdf3aef8d2 | -8.34407 | -44.95158 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d09f7b35-6477-3f47-aab2-27aca6e67b40 | -12.56922 | -46.96601 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e460a0d7-3582-396e-b96a-8300f86c3911 | -13.60668 | -46.91254 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af7e56cb-9885-327c-a182-2a71348ea30b | -8.11076 | -42.35807 | 2025-08-16 03:45:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff4d5d90-1428-3107-aa46-2b24ed84a290 | -12.60975 | -46.93665 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8f80ec7d-78ff-3071-acdf-e0c7b711e652 | -14.0457 | -46.29448 | 2025-08-16 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8755e6a-789e-3691-a0ce-55e6a2a47703 | -9.80554 | -48.54058 | 2025-08-16 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51306af3-e075-3f90-9667-66ccb2b9e1da | -13.6056 | -46.91676 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e15adf2f-424c-379b-8e3f-a3ecd8282c41 | -12.83236 | -46.02937 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df996759-9b3b-3b6b-89eb-903abdc191d6 | -12.2331 | -41.38644 | 2025-08-16 03:45:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf468f3a-4c2b-3183-a34c-14ec0e42de46 | -12.8 | -45.97256 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88da48c3-a24d-3626-b41a-59d3141d711d | -7.40828 | -44.89006 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b22400b-17ab-34af-bacd-8c4cf8dd2b75 | -7.36371 | -43.8427 | 2025-08-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d411739c-fd14-3afe-851c-76c72632dc2d | -12.55431 | -46.95317 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f19b8270-5374-3337-a8e1-bcc1ff2c419e | -12.55338 | -46.9579 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72076b45-0ab7-35ff-a765-8902b70f6de4 | -12.60853 | -46.91303 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b0470e3-f4ac-3954-a91c-8660e4bc1e4b | -9.70461 | -46.2629 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d645b290-b4ac-3cfb-8f31-78e26bb9f704 | -12.60129 | -46.98037 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c1ba747c-2e32-3f86-9e98-2e702f95a054 | -12.79664 | -45.96208 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14778e1f-1e6c-3121-a471-a2d58cd53634 | -7.39688 | -44.89198 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee8d6266-a29c-3352-8107-39f8f15bf5d5 | -12.59849 | -46.95519 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 42675935-d344-379c-b3d8-84bf66b7db47 | -9.81196 | -48.54208 | 2025-08-16 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 120ae1f6-ffb0-35e8-92a9-c79fb5758ee3 | -9.17316 | -45.32311 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0da9bb91-d546-3adc-bc37-ddb4969497ef | -11.92879 | -44.12531 | 2025-08-16 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0b5df74-7942-3e33-ae12-967d9df0b5a2 | -12.83173 | -46.03262 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1beb5894-2f37-355a-8286-3130ff3baedc | -12.55085 | -46.97073 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fceac377-12a0-3cb5-acbb-b63610d1430c | -12.60565 | -46.9485 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c7201d85-989c-3852-b2c3-5694ae593843 | -8.17376 | -45.02337 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00df186e-36c2-3603-bd6f-5b71893285d1 | -11.54907 | -47.26584 | 2025-08-16 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3a4c8848-6c47-3629-abad-029ed7d2e9fa | -9.69825 | -46.26579 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 977dd528-5429-3e0a-9e9a-02be99f4de56 | -9.80483 | -48.54531 | 2025-08-16 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18320156-cc55-3a75-afa6-d897bc1ab68e | -7.60053 | -45.20853 | 2025-08-16 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f222f189-dad5-3966-8385-5d00de946ab0 | -12.30055 | -50.01033 | 2025-08-16 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dea3e0d8-529c-3840-8077-2392febb42c8 | -12.80684 | -45.99312 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6155eeed-7da5-317a-a332-d03394f1c2d9 | -12.46884 | -46.98572 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6ee4d84-1e9b-3dcc-8bd8-0143b7d957b4 | -12.56067 | -46.95034 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d916bbe4-2ec4-3dac-842d-b3858488dae9 | -11.41636 | -44.69223 | 2025-08-16 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70b431a4-252a-31b0-a9cc-bdcb2a48eec1 | -15.50672 | -40.75543 | 2025-08-16 03:45:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ad2970c-2cba-31d4-be21-75fc2f501c10 | -12.59857 | -46.98366 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 010a9db4-2aee-3b7e-9e30-f4ffc8831a85 | -12.80732 | -45.99055 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a6434f3-34c3-3f42-8576-21c54af6a335 | -12.60648 | -46.94436 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| fdad2068-75a0-3ba4-baea-7878e209d4ec | -13.8704 | -45.55827 | 2025-08-16 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16a70691-02d4-3c2f-9903-37b8aa657914 | -12.59871 | -46.96368 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1899baba-d8ce-3226-9f64-19e8c571744f | -7.39328 | -44.91185 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1976bb84-a7b2-3ccc-9a06-534c45f5ea4d | -12.53785 | -46.94827 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 304a242d-99ec-303e-8edf-3f792df75687 | -12.83903 | -46.05114 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 853eb9cd-5d11-379a-af08-8095d074e28e | -8.16902 | -45.01909 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e41b293-c427-3cc2-acae-d57bcc2edf59 | -9.85484 | -47.81929 | 2025-08-16 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79d195f9-3009-3b44-b7ea-e889ea1d5da4 | -7.38728 | -44.91444 | 2025-08-16 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7f43963-5711-3a70-9ea3-5dfe3dd6a6b0 | -12.82571 | -46.00763 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a6e5e2f-87f2-3037-acc7-d95d24086be4 | -8.16779 | -45.02592 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eda9b07e-0c15-3a85-b50c-c2342ccb35ef | -9.70013 | -46.27319 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2b7a928-3c72-31fa-af4b-5e4af1401044 | -7.36579 | -43.83108 | 2025-08-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6119d60f-968a-3d41-b22a-c58378b97234 | -11.31197 | -42.07086 | 2025-08-16 03:45:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| de08c5b0-e542-3c99-a83b-3e46cdc2b907 | -12.60175 | -46.94803 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 279448d1-a708-3c3e-93dc-08c3e2b69a01 | -9.85317 | -44.68655 | 2025-08-16 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3ca0306-61c2-349c-a2be-97f3571a7ffc | -9.33137 | -37.98283 | 2025-08-16 03:45:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 049b86c1-31c8-39e8-82ac-a1917a6b755d | -12.46958 | -46.98193 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 481fa460-27a0-3786-a169-e1329645cd69 | -7.42182 | -44.87614 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d637057-f9ee-348e-b512-e0f56d8a911b | -12.61372 | -46.93723 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 94362d54-ef5d-3b42-9727-54928d671128 | -9.26556 | -44.54462 | 2025-08-16 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9838135-f4ec-31e5-9962-ee93cbd47a53 | -12.40645 | -47.78996 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ed44dc7-be53-3e0b-bd8a-d706d79ce8b1 | -12.80061 | -45.96946 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 197c202f-8d3b-358e-92d9-61925c9a72c1 | -12.61144 | -46.95792 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 04fe2589-2d6d-3d9a-b3bd-a1fcef7ccc8d | -12.61286 | -46.95057 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 595f4c8a-9561-3bfb-9926-ad3810ef6b9b | -13.58248 | -46.97695 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e9aa21a-8ffd-30c7-9d7f-a0c612559d98 | -15.50745 | -40.75125 | 2025-08-16 03:45:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2add7ef-6f81-30f5-b6e4-0b5382b5d7ff | -12.56207 | -46.97282 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 80cbe806-559a-3883-a2e3-77e92a56dc0a | -12.60405 | -46.95643 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6adf3192-b4cc-3290-b5ed-a84990ebcf6c | -13.60641 | -46.91256 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 114dae07-b7d8-34e7-b403-3dd02505794b | -7.55127 | -45.41949 | 2025-08-16 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 25e87faa-9a80-3aa6-90b4-06d12499f34c | -8.18565 | -45.01841 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5faa6b62-c579-3b40-aebe-cc292afe80e9 | -7.23755 | -44.79066 | 2025-08-16 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88c0b539-b5ce-3e44-aec5-ae225d36d6fe | -8.29738 | -44.9682 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08d7eef1-7de8-3f30-b904-665a7ea2f3e4 | -12.55893 | -46.95921 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e5f075f9-47ab-3a2d-b476-ae4b25e8da84 | -7.35977 | -43.83594 | 2025-08-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 753bcfa0-08eb-3ed8-88af-2d0df252cfc7 | -12.59939 | -46.97957 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 04dc953d-691b-3223-88da-5e3fd23795c7 | -12.6112 | -46.94975 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e70c84d2-55c3-3cd7-bc24-b5fee4df3d01 | -8.19449 | -45.03049 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21a16132-4d6c-3679-b15b-048f952c141b | -13.618 | -46.91291 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed27c561-62b3-3a0a-a38d-2aec6d3e6201 | -12.60791 | -45.23484 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 487c30da-cd91-31d7-930c-c87d9f11796b | -12.49174 | -47.51143 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 095697f4-ac8a-3454-b1ed-22899f383706 | -13.58293 | -46.97366 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e03361c-72dc-3575-b487-1c514b7ed99b | -12.60969 | -46.95728 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eda74146-55ab-3f11-860c-8e96873146b7 | -13.41835 | -43.68082 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4d4f6f56-9316-3048-aaca-65ebc477e8c3 | -12.81192 | -45.99479 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d46ee604-6200-3f5e-8009-711906fa8a97 | -12.2601 | -44.57931 | 2025-08-16 03:45:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11bdddf1-9624-3164-9dcb-6af28506b96f | -12.53633 | -46.95591 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4906d0fa-1eac-39c9-ae49-8942c4f1be1b | -12.52844 | -46.96638 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 436c54ff-265b-31c9-b315-d04d5d62878a | -12.80744 | -45.98992 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b20dd303-a8af-3613-a32e-a8d423670ad0 | -12.8303 | -46.01199 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09d55a19-ffce-3e88-a934-35f51ba74d05 | -11.26552 | -50.4744 | 2025-08-16 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a0572fb-88f7-3cca-8af9-0d1c7c7847eb | -13.61236 | -46.91263 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
