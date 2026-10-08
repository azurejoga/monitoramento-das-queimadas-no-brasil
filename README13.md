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
| 747467a5-edff-34fc-9a69-79ea17c081ba | -3.3052 | -54.0159 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da07c82-b8f4-31e1-a5f2-1a8f53b08c3a | -14.9077 | -48.099602 | 2026-10-08 00:26:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c8506e7-cac1-393a-b7c0-9e1dbf755106 | -2.9453 | -54.110802 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a875729-7b41-31ca-bd81-d729b6f6e55d | -3.6102 | -54.588501 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b200000-76be-374a-b108-723544b3a97b | -3.1728 | -50.600101 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca95971c-43a5-39cd-a329-35d3c50b5e57 | -2.5856 | -56.169201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48a80cbd-34f6-344f-bb2b-1def6476ade8 | -1.4981 | -54.822201 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2744a91-a544-3d6c-a8ee-a8298272bd50 | -6.6169 | -43.708 | 2026-10-08 00:26:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5923532a-2a1c-3f00-849f-e77310c46a4b | -3.0182 | -57.730301 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69f88eba-513e-300a-8f2b-ff3ed58a3143 | -3.2644 | -54.0177 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e59e9fc7-8f89-37d6-aea3-6217fe82cbab | -4.5676 | -54.948299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8616c0c9-8648-3b83-ab6e-6b6399385f2e | -3.1061 | -54.183498 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14a21fdc-3793-3ba7-9e18-6c1e386e0868 | -2.9448 | -54.1544 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a9e46b0-a217-3547-9f22-3b795d88dd0c | -3.2872 | -54.0271 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88b40091-1cfd-33e7-9a16-03948e2974fb | -2.9696 | -54.127102 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e6f565d-037f-3c98-811a-8b108ee29681 | -3.4269 | -58.595402 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d042eca4-3106-3f9e-9dc0-22d47e3577e3 | -2.9943 | -54.0998 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 500efdb5-67d7-335f-b3a4-e80d17a361fb | -2.9428 | -54.190899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc0ff3e-e7c6-3a43-82a1-f6ae05e3908c | -7.4341 | -63.518902 | 2026-10-08 00:26:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2226235-183f-3fb7-bf93-e64384c62f42 | -1.5275 | -54.815601 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d72e410-8c03-3819-88e7-ce7cb6f62e4a | -3.0238 | -54.093201 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37030337-ec52-382c-a8ba-b160a99d3e14 | -7.8803 | -54.975899 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d46349b7-368e-31e3-8709-d348a53b3199 | -4.1095 | -59.872299 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b48bd02-5392-38fd-aeef-372318e21419 | -3.5523 | -54.651501 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ceda0b-c9b7-367d-b17e-c18f60904f91 | -6.1006 | -49.413799 | 2026-10-08 00:26:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49b1720d-73e5-387a-871e-2cc645b6ef81 | -8.7132 | -45.145199 | 2026-10-08 00:26:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82d877f1-2a57-3bbe-9f66-4b94815282bc | -6.6322 | -55.289398 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a27b5b5-fb7f-36fc-a154-c8e2ec98eb42 | -5.0399 | -49.7687 | 2026-10-08 00:26:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77cb93ae-4ab9-3dfe-b1b8-07dab2e584d9 | -6.0411 | -51.7267 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e699164f-5935-3037-86c6-7678c6cbdb4c | -3.2656 | -54.068199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165f69fc-62c7-3558-b364-db36143f7cf2 | -3.0441 | -57.478298 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1819b945-e818-3dea-bcb9-06a56daa2af0 | -5.9834 | -55.381302 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eaf2ff2-9578-3b41-8564-06c6214d675b | -3.5244 | -59.312801 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a7032b3-c547-3367-97af-03415c210ce7 | -2.9339 | -54.106098 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94c59683-707a-3682-a39c-29c9573105ba | -2.9397 | -54.1772 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e587552-6035-3459-80d0-06010c86c941 | -3.719 | -55.482101 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 847c132d-a8c5-3295-a3fe-0ac0908ba644 | -17.7045 | -43.0158 | 2026-10-08 00:26:00 | METOP-B | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d8e426e1-cf86-3bf5-b8ac-ae58a3a9d77f | -3.0544 | -54.137199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31179f66-679b-370b-98fb-32d2ac14eb6a | -2.7842 | -56.5028 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8884b4eb-32cb-3b09-814a-4c1ad2bb085e | -3.5084 | -54.6399 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee6457f9-e1ae-3653-853b-62b296c2e478 | -3.477 | -59.562 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd2f26d-d637-31a9-b3bc-e1d74e26db4e | -2.4981 | -56.1007 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8feed1e8-a8d3-364e-abcf-c15f7a683078 | -3.0488 | -54.203499 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc6fc4c1-1a5e-3698-9d57-31e8a2c3c3f7 | -6.163 | -52.662399 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0869a9-8681-3096-9fd1-c166f793fed3 | -3.2032 | -50.553101 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 414a070c-3a4f-3819-9dbd-9ef9ad45e643 | -5.9575 | -55.3577 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47045b76-1858-3cf2-a41f-7803f51d671b | -7.2307 | -55.156898 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd7faa97-4fd7-363f-b59e-cb805a500271 | -3.5039 | -59.266399 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6a76f80-8e05-3ed4-ab32-92e2919277b3 | -3.1025 | -54.987598 | 2026-10-08 00:26:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3346b3cb-4275-3047-8af2-9ba6b2d7b99c | -2.7563 | -57.663898 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c31abb67-b7c6-35f2-977c-a69612f9f56a | 4.2807 | -61.0392 | 2026-10-08 00:26:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c344365-c8af-3ba7-a714-b30be18a36b2 | -4.551 | -54.9664 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd2d7bf-b751-32f4-b445-25ec0dea726f | -1.8054 | -57.097198 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2db9db5a-ae74-343e-9f35-04a10ae3ec94 | -3.4462 | -56.929001 | 2026-10-08 00:26:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b44f74f3-656a-3d46-af26-33015f550102 | -1.6045 | -55.155998 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14de43d0-8a0f-3b04-b645-b4a038b6065a | -2.8694 | -54.185699 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af41e64-9b2b-3156-8d42-4ed3c3370d95 | -3.8521 | -52.0285 | 2026-10-08 00:26:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a94bb871-6613-3aea-8f08-56d445684be3 | -2.7809 | -54.067501 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80730012-40fd-3b1f-9677-ccdab1e46b90 | -3.0512 | -53.941601 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 935b64df-727c-332c-a518-064115c14437 | -3.3275 | -58.148701 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c328ba4d-a7e7-3c70-abb6-28016667133b | -3.0595 | -53.932499 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cad8715-d197-3a43-a586-7be08c138921 | -2.9774 | -54.161598 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68abfb70-555d-3051-98a1-2d70b6c5b369 | -3.5146 | -59.314899 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c09208b-e275-343c-b44f-d1d6ba33e6f0 | -10.2465 | -49.665298 | 2026-10-08 00:26:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66dcd661-02a6-352e-b37d-854027f4a8fd | -7.1095 | -55.723499 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5abbf12e-ad09-3cea-a718-441447206341 | -4.2957 | -49.097801 | 2026-10-08 00:26:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 231cce54-170e-3411-bb31-ccd784080349 | -3.9643 | -56.115601 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1edab52-6daf-3242-b1df-3933f7e79b08 | -1.6279 | -55.122299 | 2026-10-08 00:26:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcc6ff64-7f82-33e5-b44b-307272224305 | -4.0863 | -55.328499 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c60412c9-5df0-392c-b287-09d6a8ac5887 | -5.6863 | -53.4673 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8cc82c-f38d-3be1-9046-a8a3bbcfb0e8 | -3.0354 | -54.235401 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e049003e-7b47-366a-abaa-bfc29065e5e3 | -2.4784 | -56.105 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c12fef5c-dba4-37d2-9b61-4da9f1c6a994 | -3.2513 | -56.7939 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b33c08f-6a94-343f-ad9b-96c5047249a6 | -2.4841 | -57.7812 | 2026-10-08 00:26:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9e0277d-b81e-3d26-8173-e5396617ded2 | -6.1084 | -55.665001 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c9bc9c-323f-3fab-bb2f-70c2b461845d | -4.8045 | -54.673302 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f330b7ce-eafc-3d53-8dac-cc421454b482 | -3.0021 | -54.1343 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cce9076e-2414-3120-b362-98ff2a5130e1 | -7.2213 | -55.1147 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d465b043-ecf0-3812-bd8e-d7bdfcfecc5c | -3.1682 | -58.6334 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3607378-4374-3792-9c23-0bf0e6b8cc17 | -5.7335 | -45.1464 | 2026-10-08 00:26:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d82e580c-1406-3ccc-b500-af230804e1b2 | -4.803 | -54.6665 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f63b9e-7132-3605-b28e-ae5f83c4cf4b | -2.9898 | -54.762402 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c73322d5-618c-3f38-833c-bbef12ee3e5d | 3.1602 | -60.582699 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cbdf101b-c96a-3e09-b9f2-df1890540833 | -2.9354 | -53.931 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f641a92e-6fa8-3c68-a76a-9ec29b090ac8 | -3.0416 | -54.262798 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4929e6a5-a1e2-322a-8884-835dad064371 | -4.5774 | -54.946201 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 117bf0b5-8d11-30e1-9ba4-dee01c120d99 | -3.526 | -54.671799 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b29803-8a09-32ab-9934-389dd519a742 | -13.7102 | -49.105801 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be342f56-583b-3f1d-b6a6-b1abae2e8f3e | -3.7382 | -54.653099 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19aa7dfd-2fb5-39f4-9d6a-987baa4626cb | -2.5076 | -56.326099 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0e8f4da-ff62-3637-bd2d-a251288cef46 | -7.3455 | -50.015202 | 2026-10-08 00:26:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87fd9a38-841e-3e84-913d-d1b46445b6e4 | -6.1725 | -51.938702 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c69d7c32-a0c0-35a8-8699-07250365d61a | -5.691 | -53.488098 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5504fc-cc24-323c-8680-18b85e106177 | -9.8825 | -50.490398 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 089b8eae-cf20-3aae-a8c7-dc44997aeb23 | -3.0249 | -54.1437 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f3d4e61-a221-3fce-be43-4f79b3532a43 | -2.8728 | -54.473301 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5934fae5-5684-37b2-a1f5-dabc85aa3c97 | -1.4484 | -54.466 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ed6ce6-d016-3819-8716-9e68dff7f0bd | -11.8606 | -48.030899 | 2026-10-08 00:26:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0ebc4aa-63cc-38f3-85a0-01b4c50c8b8e | -2.5106 | -56.156399 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbaeb9f0-d1f3-39e1-9697-4a5e633dc203 | -3.0288 | -53.888199 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
