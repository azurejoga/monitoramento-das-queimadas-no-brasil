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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 625318f0-83ca-399b-b093-813779380aa0 | -9.26778 | -67.60577 | 2024-10-01 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be67ff6a-222a-35eb-81cd-bb42d865a3c4 | -9.53897 | -68.60283 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea040844-0cbb-32e5-9d01-ed7c4abbb498 | -10.44923 | -67.89145 | 2024-10-01 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b092a713-43fc-3579-b30c-b541190f47e3 | -10.27403 | -68.76445 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b585c6ff-27d2-32e0-b870-610eef2cf1ed | -10.27088 | -68.76056 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4c40d94-053e-3c6e-9fd6-4b54f92c9f32 | -10.26984 | -68.7657 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe95ac8a-d63c-3117-a4fb-f791773d1565 | -10.26769 | -68.76326 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53a0861d-447b-33f2-b318-b197c0c8b2d6 | -10.13233 | -67.89803 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81a7c73c-e089-3a7d-a767-155f02e08980 | -10.13136 | -67.89514 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85501f16-80e0-35f7-b5fc-5199a961b6eb | -10.12721 | -67.89235 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3c8966f-a3fe-35b3-bf58-d0e6f66df03e | -10.12619 | -67.88949 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7f59746-b609-3e68-82cb-1ce6b82c35ad | -10.12533 | -67.894 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18663a1d-15af-355e-b51b-34d31190d6d2 | -10.12117 | -67.89125 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aebcc19f-cedc-3884-bd54-536d96713722 | -10.1193 | -67.89288 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e7f4bf5-52cc-306d-93d7-9584890b1e51 | -10.07354 | -68.23117 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89a20703-afc1-3fd7-a5cc-55674581e52e | -10.0726 | -68.23608 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d2c22e1-4469-390c-aa3c-68bb139e2cac | -10.07221 | -68.23336 | 2024-10-01 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c229654-aaf1-365a-b8b1-986efefbb376 | -11.25364 | -43.38278 | 2024-10-01 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 67e426a0-8f0c-322e-8482-29295b5afc74 | -11.25294 | -43.38125 | 2024-10-01 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 12280a40-c817-38ce-81de-ce9a8c77c8f5 | -11.2529 | -43.38932 | 2024-10-01 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 79e54fd0-d8e8-32c9-8eda-103fbdb4c401 | -11.25224 | -43.38781 | 2024-10-01 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ccfef1fa-03ba-3462-91c7-704c0dc5b18b | -11.25154 | -43.39433 | 2024-10-01 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2a86ff5b-0e21-3afd-9175-a2809819da4d | -11.24595 | -43.38841 | 2024-10-01 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e79e1e5d-772e-349d-b37c-5eb0f44c540b | -12.07465 | -44.95935 | 2024-10-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 340c6743-0da3-302d-a363-51296ee70f5d | -12.07031 | -44.95827 | 2024-10-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00c04cce-cd12-305e-82b4-fc16ebc51781 | -12.06826 | -44.95849 | 2024-10-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18e05fec-b6e3-3514-8a8a-385bac2227a3 | -11.26219 | -45.65456 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebfc8a60-ea7c-3634-a138-a5a7c39f3af8 | -11.26166 | -45.65908 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3adfd864-f26e-3628-bbf2-bf7eb88b9637 | -11.26113 | -45.66356 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07a77857-d4d2-32b9-81d0-b4120a81f3b2 | -11.2601 | -45.67232 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 849b8194-40a5-3811-9482-1f99a75b75f3 | -11.14087 | -45.68018 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb555c74-204d-3867-bb97-8380dd01464b | -11.14033 | -45.68481 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d16112f0-d942-3ec3-afc7-440784fbe4e3 | -11.13875 | -45.68205 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86b7b00f-6ac9-31f9-b750-0e6172b55a5a | -11.12596 | -45.64987 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 021a273a-30ac-35b6-a106-fa873cccce05 | -11.12461 | -45.64723 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd308296-cfce-348d-adfe-ebb6b4800d85 | -11.12404 | -45.65189 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84507a58-ba7c-38eb-8bbf-f37075e43de6 | -11.12207 | -45.63034 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00c9a357-0ade-355d-8182-b0be00aabf87 | -11.12152 | -45.63507 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d7e2b58-9e20-3056-9b0a-16b86605a5b4 | -11.12085 | -45.6277 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88885be1-3377-392f-9f0a-9aa29ea6e54c | -11.12026 | -45.63245 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3791a265-4cb9-360f-95d4-ef0fe12d9033 | -11.1199 | -45.64912 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffe0764a-c05f-3def-9228-59471edaa2f7 | -11.11969 | -45.63717 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 07f52557-bb4a-3515-986d-ac5180d4efcc | -11.11797 | -45.65117 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5055142-d19a-359d-903c-439d623768b5 | -11.11545 | -45.63435 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f450031-4b8e-3367-a40f-37dc1752efb6 | -11.11491 | -45.63905 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5f2d229-04c1-326d-a921-ded9fc6addb5 | -11.11459 | -45.67875 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3144f0d-4dad-3c55-b180-8b95b3cec273 | -11.11403 | -45.6833 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a23ef6c-077d-3606-80a8-0d3af322e962 | -11.11014 | -45.68045 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 009255ff-dcef-3785-8890-6c8d13278675 | -11.10968 | -45.66871 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73e265e5-4f57-3471-9172-b290c8b613d4 | -11.10962 | -45.685 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16be76a2-3580-3079-a6e4-9791242e5d0d | -11.10802 | -45.68228 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c814ddac-bcc0-386c-bbce-b7db8fb11f1b | -11.10517 | -45.67035 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4ce630cb-0bc4-32cf-9309-f5d2751a3694 | -11.10465 | -45.67485 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0066f4b9-10a2-31b2-8375-469d66d67c1b | -11.10365 | -45.66775 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1e1ff077-e18c-3cb0-89cb-2660f81a3de9 | -11.10311 | -45.6722 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d4465135-a508-3985-b81b-852f8c27665a | -10.87548 | -45.97698 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f9a7845-4ab4-3f52-b458-65970faef271 | -10.8713 | -45.97574 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04903b19-6af8-3f24-9f08-3e753c8bf6a2 | -10.87008 | -45.97179 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b1df5f2-3a6a-3fec-a949-1634325c1223 | -10.86593 | -45.97056 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cef1c8d-c1f1-3c46-9848-bdc3ad98df53 | -10.86057 | -45.96538 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faf50abb-3e14-3b75-9a0c-64ee92ea777c | -10.85928 | -45.96138 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e1fcdd2-792c-3c2d-b2e4-d3a06cc509c1 | -10.85877 | -45.96576 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1b013d4-075b-364d-8659-2615b8610cc7 | -10.85519 | -45.96021 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a926f7d9-e873-3306-b4a2-086e2a096be5 | -13.17886 | -46.32901 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09a28655-1500-3821-93b4-f18e4321d7ed | -13.17842 | -46.33276 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f16afd60-08a9-3d24-aa30-9da1a726f789 | -13.17643 | -46.32868 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 63257cb1-fc31-3961-98da-2a6a79aec69a | -13.17601 | -46.33249 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5ff7a5d4-193c-3080-990f-c4d2a92ca60a | -13.17557 | -46.33644 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6b4f9401-f584-34c5-af0c-232644dfb401 | -13.173 | -46.32745 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ce96f13-ffa0-38d6-a156-7a9988f92635 | -13.17253 | -46.33142 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 006bbce8-dd3d-3d0e-836e-ece967774479 | -13.17205 | -46.33558 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3edace74-b82b-3e6b-9638-ae830febd429 | -13.17155 | -46.33983 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7696095-9941-3762-af94-5854e6d3cf4d | -13.17012 | -46.33111 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4305935f-7aaf-3e22-8c9b-9e86b7cd3ca5 | -13.16917 | -46.33976 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 53f69954-351a-3d5f-a71d-323394150852 | -13.16868 | -46.34415 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ccf6d961-dc2e-3f0c-b29d-c5d5568c83d3 | -13.16559 | -46.33916 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbfb3247-1d86-39d2-8bb6-c6c1aca0214c | -13.16507 | -46.34356 | 2024-10-01 05:06:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 70cbf4fc-47c6-3894-97db-7b37c4c77901 | -14.18918 | -46.45591 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1687033-792b-3ba7-8c7b-3956f6c84054 | -14.18873 | -46.45995 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7fca4f9-6499-327a-a580-c65d941a7a18 | -14.18229 | -46.46335 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b87aa8a3-cecf-3f9c-8f05-5db364cad8f4 | -14.18178 | -46.46787 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff7d323b-c5d2-309b-acbd-b706ce736ca1 | -14.17575 | -46.46767 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeb95828-a49e-318d-a2b1-27598e1a6363 | -14.17025 | -46.46267 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81794e71-d544-3fb4-90b2-4789fe317c8d | -14.16522 | -46.4533 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b0f0e31-4f90-3a1a-9dfe-329f23054d00 | -14.16474 | -46.45771 | 2024-10-01 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84a03617-d582-3335-a49b-4ad9e2e8bf5f | -15.21087 | -46.23035 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f492e3a5-5ff0-39d7-983c-05b9beb9485c | -15.19184 | -46.23376 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e8dd21-86fb-329c-bd45-c8bd7a7ed681 | -15.19174 | -46.23417 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c326b67b-3ad0-36cd-8be7-c54269f87c3a | -15.18519 | -46.23779 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f99f13cd-9e5a-38de-8140-1ec609ab2b8a | -15.18512 | -46.23819 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79a418ba-d5a0-3171-a113-f397f729ef34 | -10.70491 | -46.17139 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b63136-e335-3f8d-9b77-b4729e6162f1 | -10.69963 | -46.16623 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0937962-ba68-396b-a4cb-bf852fba5c89 | -10.69376 | -46.16574 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7718de93-5677-3214-9fca-e1c5d0750c04 | -10.68845 | -46.1608 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a82f2c7e-e4e5-32e3-8d6d-b4597a36f94a | -10.68315 | -46.15563 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ace37ec-2506-373b-8ead-50ffa613151b | -10.68262 | -46.16003 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e19dcc3-d772-31c3-9777-a2a85fa909bd | -10.67733 | -46.1548 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da8b1e4-2354-36ec-8aee-2984293329f9 | -10.52592 | -46.04169 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61fb8c4a-792a-3280-a8be-90eb73a98271 | -10.52007 | -46.04085 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8660fd38-ce75-3e9a-ae1a-e697e6344de1 | -10.51423 | -46.03987 | 2024-10-01 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README105.md)
