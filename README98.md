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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcfe5f27-ec5e-3920-bec2-8c6532704a40 | -18.0059 | -57.36427 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 0d5fbdf2-3f9a-3cc0-bd96-dea9dee28338 | -18.0051 | -57.36886 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aa8fcec2-d112-3fb8-aa3b-c05d038d59e5 | -18.00429 | -57.37347 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8a1bcc9b-0013-3377-8933-dccde79c4468 | -18.00139 | -57.36814 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b45989db-2ad8-32c7-8a07-d8bb81abd92b | -18.00059 | -57.37275 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9a0bbf54-9fd5-3aa5-8c4d-91f97c527d4d | -17.99769 | -57.36743 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e556266c-edcb-324b-a866-5360f0586c7a | -17.99688 | -57.37202 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4248d4ec-e24f-39a8-af17-f82874aceb30 | -17.99236 | -57.37591 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8f0c657e-2888-3fe8-bb12-c961f28aaac9 | -17.98205 | -57.36914 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e6ca7dbb-8775-3ad7-a7f0-fd7509e2a85b | -17.97997 | -57.35922 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 8bdd1f06-f5a8-3a2d-86eb-0fca3092f092 | -17.97834 | -57.36841 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 380e545c-e04b-39df-8d77-97bff768b70b | -17.97545 | -57.36309 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b81621a-b508-3218-80ec-163a3275a0a2 | -17.97463 | -57.36769 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9d28e1c2-c765-3fe7-90f5-f62d742b79b6 | -17.97093 | -57.36697 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 775fe0a2-52bf-3c7d-b9c8-2440b93a033c | -17.96144 | -57.35561 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e5204457-0555-3965-a4c8-b1119db069f7 | -17.95528 | -57.36869 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ae01fe6a-1833-35d3-b628-7c4523cf1c02 | -17.95075 | -57.37257 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 24d58498-a1b8-3a63-8d23-419119ed11bf | -17.94994 | -57.37717 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 7b624a3f-c0bf-30e6-ace7-ba821baa2bae | -17.9495 | -57.35804 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 488c704a-354e-3ec3-993d-46d868817824 | -17.94786 | -57.36724 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 6aebfd8b-0f21-3083-b334-68f146db51e8 | -17.94705 | -57.37184 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 807a0c05-113c-3a54-aff5-9915293e6778 | -17.94622 | -57.37645 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| f164a476-6e72-303b-87d7-b7102268cab1 | -17.94045 | -57.3658 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 863fe052-22c4-3ff3-ab3e-79adc6708c40 | -17.93674 | -57.36508 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| ea0bceee-9a21-360e-86e5-c40db81612cd | -17.93221 | -57.36895 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| cc2fde1a-f592-3e59-818a-479138455bc0 | -17.93015 | -57.359 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| bacafe47-c242-311f-97ab-6009e376eae8 | -18.02233 | -57.35797 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 87dafcb0-e6e5-35e6-a0e9-c4dc3f418378 | -18.02049 | -57.35531 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 06408da2-77be-321a-8873-751cc37cc1a5 | -18.01862 | -57.35724 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 982b296d-b3d1-3506-884b-a6c90e41c7f4 | -18.01782 | -57.36185 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 8da0cd36-3a27-3dea-94bc-4e5a6db825d3 | -18.003 | -57.35896 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| d08bc33c-d4f9-3e80-898b-210d495e7974 | -17.9993 | -57.35823 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| afcb56d1-b0a5-34b9-9528-0c422f08e753 | -17.98819 | -57.35606 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bb18a11c-69c9-31fb-b85d-9970ae6fc578 | -17.98286 | -57.36454 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4759b09c-f2dd-30f7-952b-d34ca60d3ad7 | -17.94209 | -57.35659 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 82408a07-e1f0-3209-a1df-61b7cee07e6a | -17.92933 | -57.3636 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 92c6a86b-ef18-3a65-be18-b1b9e72b4bf6 | -17.92645 | -57.3583 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 6df234f6-3410-366a-a84a-95d3d0956563 | -17.92563 | -57.36286 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| e3d00ae9-6cb2-3289-ab0d-c8386c128c69 | -17.12007 | -57.46805 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c0e09af2-b4b5-30ea-a137-5a26af196900 | -17.11546 | -57.47207 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| be4849d7-18c2-3029-8531-6f85f0732411 | -17.05156 | -57.37163 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 619769c3-1cc3-3156-8ac4-50b454bb7df7 | -17.02919 | -57.43082 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 84966d1a-807e-3702-a6cf-0a23871d989d | -17.02747 | -57.4403 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4d91eaa3-f1ce-38ec-8b2c-44c02387244d | -17.02579 | -57.43317 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d3bd701e-c744-3f93-b4c3-a2207b8b1eac | -17.02496 | -57.43792 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3f8eddf2-8a84-3f4c-9ca7-2241cbea2d82 | -17.02202 | -57.43245 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6b1e4036-9c8a-3cd7-9a57-4192b682911d | -17.02119 | -57.43719 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6c70b78f-05cc-3486-9d1a-1dfacf51945c | -17.02075 | -57.41748 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a82f135a-8c1f-338e-9d82-8659169270b1 | -17.02036 | -57.44194 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e9d25e4e-447a-3505-9b38-431cfe00b7b3 | -17.01992 | -57.42223 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c148490e-6950-3af4-94ed-5a9f26daf689 | -17.01909 | -57.42697 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 44e78f73-7792-3573-a305-45b7fecb62a8 | -17.01825 | -57.43171 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9a19af9c-2bf0-38b0-8566-c50dbbaaa655 | -17.01742 | -57.43647 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 884544e6-4728-3e7b-957c-70f324729bcb | -17.01658 | -57.44122 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 40f52060-3a42-3f38-b97e-409c1402b3ac | -17.01365 | -57.43575 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6369e246-0792-3148-9b2d-a5c347b08252 | -17.01238 | -57.42076 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4b885127-6d69-39d2-85cd-df996e6ade47 | -17.00737 | -57.44928 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 517d18f3-2309-355c-8bed-881bbd22f2eb | -17.00651 | -57.40983 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2d741df9-baba-3882-9e4d-39927b9d67b8 | -17.00401 | -57.42406 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f673d680-399b-3cad-b9dc-98045d73a049 | -17.00317 | -57.47311 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3f10d058-b29d-364d-b7a0-36dbd8bee326 | -17.00275 | -57.45331 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d71c19ff-1204-3620-bdb8-ec2af949be4d | -17.00275 | -57.40911 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 87a7efbc-3a33-31fb-ac25-58c060a94535 | -17.00191 | -57.41385 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fd5a39ae-cf1c-3b78-ac0f-06cb1988fb2a | -17.00024 | -57.42333 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f472816b-2e76-35b7-bba1-53a652e202c6 | -17.00023 | -57.46761 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 389157b2-1688-3fde-a124-2c78af3c7579 | -16.9994 | -57.42807 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f5ac9a55-27df-31ae-95ad-9b756081a610 | -16.99898 | -57.40837 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 65149aba-618e-35d4-bcfd-825343063e1b | -16.99814 | -57.41311 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| a6c68d10-a15c-373a-b365-dea5ef0db30d | -16.99731 | -57.41785 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b7aea6a-c03b-38e6-a23a-4288ae18c600 | -16.99647 | -57.4226 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0e5e96e7-1503-30cf-8c75-4c53200223e8 | -16.99561 | -57.47165 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 19f2836e-daed-3a2c-9c39-5d8ab8f8f416 | -16.99354 | -57.41713 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8995bccb-b7c8-3762-a26c-59b8136f5f14 | -16.99014 | -57.48048 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fa0b196e-9f54-3b5a-a1b9-0b3fb8ce2d97 | -16.9893 | -57.48525 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0d08730c-b648-3f27-807d-3ec227023924 | -16.98636 | -57.47974 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e6736674-430f-3ef0-8f07-58a062d0b8f6 | -16.98467 | -57.4893 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 69c6ab61-2e4a-371f-b914-fc2deb23f846 | -16.95304 | -57.51294 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 39a49dc3-03c1-345a-8f97-bfcbb43e123c | -16.95097 | -57.50261 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eb230ff6-db49-362c-ab02-3b983f6d37b5 | -16.95011 | -57.5074 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a4d31a7e-bf38-3782-a7b3-6588f0e89b7b | -16.94925 | -57.5122 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| aaed0aa6-ebf9-3eae-bad1-70d3f343b228 | -16.94718 | -57.50187 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 902acb6b-39da-363b-8c18-c69620e8c46e | -16.94632 | -57.50667 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 92a77e03-73f7-34e0-81c5-056c79960fbc | -16.93911 | -57.70122 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dac4b04f-fd18-3936-9c82-7882fc2f39aa | -16.85013 | -57.43637 | 2024-10-14 04:49:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 196fe783-52ce-3d6f-b6da-4352adbc1072 | -17.99526 | -57.38124 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c1c5f0eb-5cb1-37ec-9d2a-e96bd44488a3 | -17.99155 | -57.38052 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 86a09892-9d75-3901-9618-beb6f5dfe635 | -17.98703 | -57.3844 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6b4bff50-6cb6-33ae-83f9-249fd014bb42 | -17.98332 | -57.38368 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 12380f90-71e3-3358-9d4e-df10a4359960 | -17.98251 | -57.38829 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f3bf3ee9-8d33-3a04-aed8-5b9c87615528 | -17.9788 | -57.38756 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9b891d2d-7070-392d-887c-55a210dc4f76 | -17.9759 | -57.38223 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| cf3c484f-bda0-3cce-a782-78092f0cc455 | -17.97509 | -57.38683 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 2f647f2e-cb5e-30cf-80c1-3e4167f57380 | -17.97219 | -57.3815 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f326a066-648c-387d-b477-ba6ffb3381f1 | -17.96893 | -57.39995 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| 25da1a27-f175-31f0-977e-5343623635d6 | -17.96811 | -57.40458 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| f7cb5e87-1dd6-3ef2-ba66-7bcd70fccdfe | -17.96522 | -57.39923 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| b37ec82e-db05-3def-819d-09153076ca7a | -17.9644 | -57.40385 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| d9b0c3a9-0df8-39d3-8658-1610f43aa2e6 | -17.96358 | -57.40848 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 8410851c-e7df-3430-9b5d-b1f87a01059c | -17.9615 | -57.39851 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| d1ee6112-ed10-3b0a-80ac-963dd1e5fcc4 | -17.96068 | -57.40313 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |


[Clique aqui para ver as próximas entradas](README99.md)
