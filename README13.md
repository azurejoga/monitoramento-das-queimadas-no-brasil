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
| e330e558-5830-37f7-8d87-02041e13ba41 | -8.5629 | -55.301601 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54ba096d-454f-339d-815e-fac51e092448 | -8.4963 | -54.866901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0108a3e-cf7a-3d4b-9bf7-1fc3db32dc0e | -7.9665 | -44.645302 | 2026-08-20 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17b817b8-bd2e-3a2c-9548-e056f2dc4a46 | -8.5651 | -54.669201 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7a5633-f123-36bf-aed5-dafb191c5b37 | -6.4412 | -52.7341 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 721c95e5-c6cc-355e-93df-8e61bbab34fd | -8.5556 | -54.809799 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c27bf9e4-ba85-33d3-806b-1c6a2f5ef49f | -21.871401 | -46.554001 | 2026-08-20 01:02:00 | METOP-C | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 234f4e68-5fc4-3ee1-8d7c-f676524e0c81 | -4.9587 | -56.263699 | 2026-08-20 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3714a5a-194e-3088-814e-a514834369e0 | -8.5061 | -54.8647 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4b4349a-8e75-32f5-b94e-447c48354242 | -8.5772 | -54.768501 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0bae2de-2ea6-3f57-a7b9-257cc7e0b0b7 | -8.5718 | -54.653198 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe16d22-7105-38fa-bdae-f38bf7849153 | -14.2399 | -53.101898 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbf5e495-2206-3635-9271-5d20f8a95e2e | -11.1788 | -54.0149 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad6de84b-2a51-3cbd-90cb-211f0bf935f3 | -6.7094 | -59.0961 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a53a8e7-c7ed-3fe3-87dd-2f934c727336 | -14.3509 | -51.902699 | 2026-08-20 01:02:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae284d73-6b17-3828-bc60-238ac4176050 | -7.9718 | -44.666401 | 2026-08-20 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8b72af2-37fd-3b5e-9dd8-142b392b5131 | -9.1183 | -61.5872 | 2026-08-20 01:02:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 502274e9-e7f8-3d79-80ca-85d29973cfb8 | -6.5912 | -58.977699 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b38ac944-597b-317f-a894-bf235e16fb39 | -7.5591 | -55.554199 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 727be79d-78f8-355e-be68-f019c9c77abb | -8.5733 | -54.660099 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24c18abe-0c29-3bf9-adc7-6c6c8aa38dbf | -6.6402 | -56.415001 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 675a4988-0b08-352f-89ce-92c40ac9f7e3 | -9.4998 | -51.682301 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba3b7a24-7b91-3a61-a534-6e32fb2c8193 | -13.4418 | -57.067402 | 2026-08-20 01:02:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57cd516a-f234-33ea-a541-c8a8ad0321de | -7.3396 | -55.677299 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bbb053e-e43d-3915-b30d-94d800adfd0b | -8.5678 | -54.726898 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8eb50aa-d352-3c38-bcc6-f2b69fef8468 | -6.6974 | -59.088299 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4621608-efa2-3737-8d56-a437f130bc17 | -10.449 | -54.665501 | 2026-08-20 01:02:00 | METOP-C | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af7280d8-4fb4-3f4a-be37-3dfecc893de0 | -7.5329 | -55.574902 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b309e89-5f07-3d0c-bac6-95ef2b359a97 | -14.0284 | -53.6334 | 2026-08-20 01:02:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14785e99-d71d-3d3e-b773-0ce9d4e2fde2 | -8.519 | -54.876499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c13aee8-0827-3a3d-b69c-0fa11576b468 | -4.273 | -46.514 | 2026-08-20 01:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df398043-b9b7-3c4e-a491-ce7df1224753 | -6.6996 | -59.098202 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e05d82e8-0f12-3e74-8fd4-46b680c3d95b | -8.1009 | -51.6609 | 2026-08-20 01:02:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 464abcc8-73c2-3927-a0ab-512699bebf09 | -6.6876 | -59.090401 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81a33dcd-f5a7-32da-b2ad-bbcd57effd7e | -5.8047 | -55.722099 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ada91421-100d-37d2-8a04-1edf9d117191 | -8.6761 | -54.658901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2abca5ab-c3dc-326b-9e35-0a0ca00928f5 | -7.4759 | -55.321602 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a247e88-e76a-3be2-9269-081ec45e11d6 | -17.3349 | -43.640701 | 2026-08-20 01:02:00 | METOP-C | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd9f1a32-d670-32ad-8cd6-ee709785a459 | -9.1225 | -51.130199 | 2026-08-20 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8017b16-e071-3395-921d-fa42e6d3a02e | -6.248 | -55.404598 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d6e70c-7120-3b1a-bada-9d0ee25361e6 | -6.802 | -59.004002 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c53c536b-6bbf-3d5d-83bd-05d4b99bf0e0 | -21.4517 | -48.513 | 2026-08-20 01:02:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b9246fad-ba4d-38d3-99be-1f984520bf22 | -14.2221 | -52.884102 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c53ec55d-6ecb-3840-83f5-3943c52d5a3d | -6.6926 | -58.925499 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f793909-1d5d-3d09-ab8e-fd1cbb52b602 | -8.538 | -54.777302 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d199e06-8f5f-3c18-a4ea-99f85da53ced | -6.2316 | -55.6054 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97fb8028-5c2e-3a45-bc3c-3cd949a02cb7 | -8.6663 | -54.661098 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd14af6a-9607-3604-ab38-e6389062d450 | -8.5159 | -54.862499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a03b7c13-7ce3-3f93-81b5-822fca1f09c3 | -12.817 | -48.430302 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc4c1ece-c19a-32b8-8717-bb8b69e9a6b1 | -6.4382 | -52.765598 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f968899-c31c-3e4e-bb2e-4b9a748a46bb | -8.5524 | -54.795898 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8809a5f0-69f8-3ba0-be6f-fba2e37cbc82 | -8.5509 | -54.789001 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 343fc27d-583e-3efe-a86c-b24411642a66 | -16.496401 | -55.176899 | 2026-08-20 01:02:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62f892cc-0949-3900-b465-cab07cd4085b | -14.2237 | -52.891102 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83fffbe3-dc78-33e2-86ad-b9fa8d810481 | -14.1572 | -53.054501 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f1631c4-92ad-3ad9-8bc1-72b7cb96511a | -6.3883 | -54.9319 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4fc9cc5-6016-30c4-87a9-5c9a0eadadf4 | -7.5509 | -55.563499 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a4b54c-471a-35cb-8890-787415af503e | -6.7051 | -59.076302 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfd7377-b260-340b-bdc5-e9cc3193a82a | -7.4482 | -60.000999 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea3f4ba2-7dfd-3667-8166-fbbf7982af39 | -14.2252 | -52.898201 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7cc6e69-2024-3fdd-b618-1d06eb72ab35 | -11.4207 | -54.313801 | 2026-08-20 01:02:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3255e9e-0125-34a5-abbe-0fb8c8ef8d7b | -18.0263 | -44.600899 | 2026-08-20 01:02:00 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eeb2db8b-4bfc-3a99-b58f-a59a06eca6de | -6.9521 | -52.801201 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58090a97-a06c-303e-a530-4e13ece20ab2 | -9.113 | -60.341599 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a720c799-0742-307c-95a9-655ad171d0e5 | -4.9603 | -56.270802 | 2026-08-20 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5752d3cb-1be3-311c-aca9-8a7718875065 | -8.501 | -54.887798 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1ed516c-131e-34b9-818e-1be14c6a275a | -14.201 | -52.881699 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b8fa5c3c-b95b-3ac5-8d65-79b08eb8a2eb | -7.6164 | -45.1702 | 2026-08-20 01:02:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| adfa6427-e9fe-374a-9f4a-b27edfbe1052 | -15.842 | -50.887199 | 2026-08-20 01:02:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 29227fba-2314-36e7-8787-64fe04cd658b | -12.4833 | -54.745098 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c155470f-46ad-3280-8f3c-860d0c7804ea | -6.8574 | -59.022999 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0991d3b8-f378-33fe-bb59-bfb39ecbb117 | -11.1968 | -54.003502 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb309533-08a4-350b-87cf-50dc375bea9a | -7.5458 | -55.586899 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31ceb2c4-faf0-3697-bf76-4ab21751bc37 | -12.0059 | -53.431301 | 2026-08-20 01:02:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb7aca9-263d-3690-b100-e29f786bad1a | -4.3874 | -55.471401 | 2026-08-20 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae4a98bf-9e42-359c-8ef0-a4d040610153 | -10.8367 | -50.297001 | 2026-08-20 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b44bbdb8-107a-3124-9910-4625f07b826e | -6.9541 | -59.043701 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6e75ece-2fbb-3bf2-a34d-9daf6a9be48d | -3.0965 | -61.2029 | 2026-08-20 01:02:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f129d992-a0c0-3cfe-89dc-111628b302f8 | -6.0889 | -57.909901 | 2026-08-20 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8086bd40-f7e5-34d4-83c2-3f5313179661 | -10.7956 | -50.297901 | 2026-08-20 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3056887-fb5f-369c-9e0a-55f07d15c692 | -10.9052 | -56.3652 | 2026-08-20 01:02:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06447eab-8b4c-3a01-8e6f-d0f0b30c701d | -6.3127 | -55.919601 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e31d1fb0-3f31-3a21-9328-f4e010e34c52 | -21.873899 | -46.5639 | 2026-08-20 01:02:00 | METOP-C | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c8eaf72-4486-3b20-bb47-21f0ab3c2b97 | -9.3901 | -60.545799 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1f032f2-b9fd-3c6a-8f26-717693245be3 | -8.5364 | -54.770302 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b3b215-6aa9-3d74-bfd4-18179dd5678b | -14.2025 | -52.888699 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47bb09d6-f88f-342b-83eb-464d09079e1a | -11.2051 | -53.994202 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b75f05b5-659e-3a79-9c31-fff219eead28 | -18.039801 | -44.612701 | 2026-08-20 01:02:00 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99d65f97-4c04-3d46-bc50-719ccdd3011b | -21.716299 | -47.148998 | 2026-08-20 01:02:00 | METOP-C | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fef8a223-a5f4-380e-9bc0-9c29891c46ee | -7.7528 | -49.193298 | 2026-08-20 01:02:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 490dca9e-e06f-3977-927e-10144567ad30 | -9.1282 | -51.154301 | 2026-08-20 01:02:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 344443ee-fa01-3989-87ca-e662d91daa0b | -6.2413 | -55.420601 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4589e4d4-9bcf-3f75-9277-b816bf4c00b3 | -7.5994 | -60.945999 | 2026-08-20 01:02:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7796b0f6-922a-31db-9ac3-a44c985525ad | -9.498 | -51.674801 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20f48695-112d-3985-8e1c-50f020dff8c4 | -10.322 | -57.5606 | 2026-08-20 01:02:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c59662e3-4051-3dcf-8e28-1804573dc8f6 | -6.5968 | -58.9562 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12f4451e-b099-3c0f-8a4b-a5a184356311 | -8.4994 | -54.880901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f951636-2fed-3eb6-b35a-e601d6249c36 | -10.2493 | -54.3713 | 2026-08-20 01:02:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7658725-0c85-320a-88ae-7cbabc450ee3 | -10.6304 | -51.615601 | 2026-08-20 01:02:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a700311f-de13-3592-956f-8f0a68b2197a | -11.218 | -54.006001 | 2026-08-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
